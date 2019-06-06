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
#from viuinterfacedefinitions import VIU_OPERATION, TESTS_TO_DO, TEST_STATUS, VIU_TEST_DESC, VIU_TEST_OP, VIU_TEST_ENABLED, VIU_TEST_RESPONSE, VIU_TEST_RESULT

logger = logging.getLogger(__name__)

class viuInterface(object):

    @staticmethod
    def packMessage(msg_op_type, msg_data):
        packet_data = []
        packet_data.append(0x02)
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
        is_valid = (msg_crc_high == crc16_high) and (msg_crc_low == crc16_low) and (msg_data[0] == 0x02) and (msg_data[len(msg_data)-1] == 0x04)
        msg_type = msg_data[1] 
        msg_data = packet_data
        return [is_valid, msg_type, msg_data]

    @staticmethod
    def sendCommandAndGetResponse(op, cmd, timeout):
        result = None
        try:
            cmd_data = bytes(cmd,'ISO-8859-1')
            sp = SerialPortUtil.getPortBySerialNumber(appsettings.FTDI_serialNumber)
            if sp == None:
                raise Exception("ViuInterface", "No pic32 serial device " + appsettings.FTDI_serialNumber + " found!")
            sct = SerialCommThread(None, sp, appsettings.FTDI_baudRate, appsettings.FTDI_serialNumber, viuInterface.packMessage(op, cmd_data), b'\x04',timeout,5)
            sct.start()
            sct.join()
            print("serial thread stopped")
            if sct.stopped() == False:
                e="serial thread not stopped"
                print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
            
            data = serial_cmd_result[0]
            result = None
            if data != None:
                result = viuInterface.decodeMessage(data)
            else:
                result = None
        except Exception as e:
            print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
        return result

    @staticmethod
    def decodeMessage(data):
        [_isvalid, _op, _msg] = viuInterface.unpackMessage(data)
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
            result = ['ACTION', response]
        
        if 'manufacturing_testing_activated:' in ''.join(str( bytes(_msg), 'ISO-8859-1') ):
            #print('OHH, manufacturing_testing_activated')
            mystr = ''.join(str( bytes(_msg)))
            response =  mystr.split(":", 1)[1]
            response = response[1:len(response)-1]
            result = ['ACTION', 'PASS']

        return result

if __name__ == '__main__':
    print("tests")
