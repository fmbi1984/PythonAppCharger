import logging
from time import sleep, time

import crcmod
#from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import QEventLoop, QObject

import SerialPortUtil

import appsettings

from communicate import Communicate
from serialcommthread import SerialCommThread, serial_cmd_result
from clientcommthread import ClientCommThread, client_cmd_result

logger = logging.getLogger(__name__)

class devInterface(object):

    @staticmethod
    def packMessage(address, msg_op_type, msg_data):
        packet_data = []
        packet_data.append(0x02)
        if address != None:
            packet_data.append(address) # address
        packet_data.append(msg_op_type)
        packet_data.extend(msg_data)
        xmodem_crc_func = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
        crc16 = xmodem_crc_func(bytes(msg_data[0:len(msg_data)]))
        crc16_high, crc16_low = crc16 >> 8, crc16 & 0x00FF
        packet_data.extend([0x03, crc16_low, crc16_high, 0x04])
        return packet_data

    @staticmethod
    def unpackMessage(msg_data):
        packet_data = msg_data[2:len(msg_data)-4]
        xmodem_crc_func = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
        crc16 = xmodem_crc_func(bytes(packet_data[0:len(packet_data)]))
        crc16_high, crc16_low = crc16 >> 8, crc16 & 0x00FF
        msg_crc_high, msg_crc_low = msg_data[len(msg_data)-2:len(msg_data)-1][0], msg_data[len(msg_data)-3:len(msg_data)-2][0]
        is_valid = False
        #is_valid = (msg_crc_high == crc16_high) and (msg_crc_low == crc16_low) and (msg_data[0] == 0x02) and (msg_data[len(msg_data)-1] == 0x04)
        msg_type = msg_data[1]
        msg_data = packet_data
        return [is_valid, msg_type, msg_data]

    @staticmethod
    def sendCommandAndGetResponse(address, op, cmd, timeout):
        result = None
        try:
            cmd_data = bytes(cmd,'ISO-8859-1')
            p_data = devInterface.packMessage(address, op, cmd_data)

            if appsettings.useDongle == True:
                print("Test Mac")
                sp = SerialPortUtil.getFirstPortByVID_PID(0x1a86,0x7523)
            else:
                print("Test Raspbian")
                sp = SerialPortUtil.getPortByName("/dev/ttyS0")
                print(sp)
            #sp = SerialPortUtil.getPortBySerialNumber(appsettings.FTDI_serialNumber)
            #sp = SerialPortUtil.getFirstPortByVID_PID(0x067b,0x2303)
            #sp = SerialPortUtil.getFirstPortByVID_PID(0x10c4,0xea60)
            if sp == None:
                raise Exception("devInterface", "No serial device found!")
            sct = SerialCommThread(None, sp, appsettings.FTDI_baudRate, p_data, b'\x04',timeout,5)
            sct.start()
            sct.join()
            print("serial thread stopped")
            if sct.stopped() == False:
                e="serial thread not stopped"
                print("\033[1;31;40m"+str(e)+"\033[0;37;40m")

            data = serial_cmd_result[0]
            print("Frank:")
            print(data)
            result = None
            if data != None:
                result = devInterface.decodeMessage(data)
            else:
                result = None
        except Exception as e:
            print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
        return result

    @staticmethod
    def sendClientCommandAndGetResponse(hostname, address, op, cmd, timeout):
        result = None

        try:
            cmd_data = bytes(cmd,'ISO-8859-1')
            p_data = devInterface.packMessage(address, op, cmd_data)

            if hostname == None:
                raise Exception("devInterface", "No hostname device found!")
            sct = ClientCommThread(None, 'raspberrypi.local', p_data, b'\x04',timeout,1)
            sct.start()
            sct.join()
            print("client thread stopped")
            if sct.stopped() == False:
                e="client thread not stopped"
                print("\033[1;31;40m"+str(e)+"\033[0;37;40m")

            data = client_cmd_result[0]
            print("Frank:")
            print(data)
            result = None
            if data != None:
                result = devInterface.decodeMessage(data)
            else:
                result = None
        except Exception as e:
            print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
        return result

    @staticmethod
    def decodeMessage(data):
        [_isvalid, _op, _msg] = devInterface.unpackMessage(data)
        result = None
        mystr = ''.join(str( bytes(_msg), 'ISO-8859-1'))
        print(mystr)


        if 'PASS:' in ''.join(str( bytes(_msg), 'ISO-8859-1') ):
            #print('YEAH, PASS!')
            mystr = ''.join(str( bytes(_msg)))
            response =  mystr.split(":", 1)[1]
            response = response[1:len(response)-1]
            result = ['PASS', response]

        if 'FAIL:' in ''.join(str( bytes(_msg), 'ISO-8859-1') ):
            #print('OOPS, FAIL!')
            mystr = ''.join(str( bytes(_msg)))
            response =  mystr.split(":", 1)[1]
            response = response[1:len(response)-1]
            result = ['FAIL', response]

        if 'ACTION:' in ''.join(str( bytes(_msg), 'ISO-8859-1') ):
            #print('OHH, ACTION!')
            mystr = ''.join(str( bytes(_msg)))
            response =  mystr.split(":", 1)[1]
            response = response[1:len(response)-1]
            result = ['ACTION', response]

        if 'VALUE:' in ''.join(str( bytes(_msg), 'ISO-8859-1') ):
            #print('OHH, VALUE!')
            mystr = ''.join(str( bytes(_msg)))
            response =  mystr.split(":", 1)[1]
            response = response[1:len(response)-1]
            result = ['VALUE', response]

        return result


    @staticmethod
    def packMessageFake(address, msg_op_type, msg_data):
        packet_data = []
        packet_data.append(0x02)
        if address != None:
            packet_data.append(address) # address
        packet_data.append(msg_op_type)
        packet_data.extend(msg_data)
        xmodem_crc_func = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
        crc16 = xmodem_crc_func(bytes(msg_data[0:len(msg_data)]))
        crc16_high, crc16_low = crc16 >> 8, crc16 & 0x00FF
        packet_data.extend([0x03, crc16_low, crc16_high])
        return packet_data

    @staticmethod
    def sendCommandAndGetResponseFake(address, op, cmd, timeout):
        result = None
        try:
            cmd_data = bytes(cmd,'ISO-8859-1')
            p_data = devInterface.packMessageFake(address, op, cmd_data)
            #sp = SerialPortUtil.getPortBySerialNumber(appsettings.FTDI_serialNumber)
            #sp = SerialPortUtil.getFirstPortByVID_PID(0x067b,0x2303)
            sp = SerialPortUtil.getFirstPortByVID_PID(0x1a86,0x7523)
            #sp = SerialPortUtil.getFirstPortByVID_PID(0x10c4,0xea60)
            if sp == None:
                raise Exception("devInterface", "No serial device " + appsettings.FTDI_serialNumber + " found!")
            sct = SerialCommThread(None, sp, appsettings.FTDI_baudRate, p_data, b'\x04',timeout,5)
            sct.start()
            sct.join()
            print("serial thread stopped")
            if sct.stopped() == False:
                e="serial thread not stopped"
                print("\033[1;31;40m"+str(e)+"\033[0;37;40m")

            data = serial_cmd_result[0]
            result = None
            if data != None:
                result = devInterface.decodeMessage(data)
            else:
                result = None
        except Exception as e:
            print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
        return result


if __name__ == '__main__':
    print("tests")
