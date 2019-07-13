import socket
import sys
from _thread import start_new_thread

import USBUtils
import SerialPortUtil
import StringUtils
from serialcommthread import SerialCommThread, serial_cmd_result

from time import sleep, time

import serial
import appsettings

'''
_dataByteArray = []
_dataBytesLiteral = b''
_packet_being_received = False
_begin_char = b'\x02'
_end_char = b'\x04'

_flagcommand = False
_msgwasreceived = False

'''

HOST = 'raspberrypi.local' # all availabe interfaces
PORT = 65433 # arbitrary non privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except socket.error as msg:
    print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

s.listen(10)
print("Listening...")

# The code below is what you're looking for ############

def client_thread(conn):
    

    while True:
        p_data = conn.recv(1024)
        if not p_data:
            break
        
        result = None
        data = None
        try:
            #cmd_data = bytes(cmd,'ISO-8859-1')
            #p_data = devInterface.packMessage(address, op, cmd_data)

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
            print(p_data)
            sct = SerialCommThread(None, sp, appsettings.FTDI_baudRate, p_data, b'\x04',1,5)
            sct.start()
            sct.join()
            #print("serial thread stopped")
            #if sct.stopped() == False:
            #    e="serial thread not stopped"
            #    print("\033[1;31;40m"+str(e)+"\033[0;37;40m")

            data = serial_cmd_result[0]
            print(data)
            '''
            result = None
            if data != None:
                result = devInterface.decodeMessage(data)
            else:
                result = None
            '''
        except Exception as e:
            print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
        #return result
        
        '''
        sp = None
        if appsettings.useDongle == True:
            print("Test Mac")
            sp = SerialPortUtil.getFirstPortByVID_PID(0x1a86,0x7523)
        else:
            print("Test Raspbian")
            sp = SerialPortUtil.getPortByName("/dev/ttyS0")
        sp.baudrate = 115200
        sp.timeout = 10
        sp.flushInput()
        sp.flushOutput()


        if not sp.is_open:
            sp.open()
        
        
        sp.write(data)
        #sleep(.002)

        while sp.inWaiting()>0:
            n = sp.inWaiting()
            for _ in range(0, n):
                reading = sp.read(1)
                print("reading")
                if len(reading) > 0:
                    handle_data(reading)
                    print("reading > 0")
        
        sp.close()
        '''
        #reply = b'OK . . '
        #reply = serial_cmd_result[0]
        #print('Received', repr(data))
        conn.sendall(bytes(data))
    print("[-] Closed connection")
    conn.close()

'''
def addcbuff(c):
    if c == _end_char:
        _dataByteArray.append(ord(c))
        _dataBytesLiteral = ''.join(str( bytes(_dataByteArray), 'ISO-8859-1') )
        _flag_command = True
        process_data()
        #print(c)
        _packet_being_received = False
        #print("END")
    elif (c == _begin_char) and (len(_dataByteArray)<2):
        #print("BEGIN")
        _packet_being_received = True
        _flagcommand = False
        inicbuff()
        _dataByteArray.append(ord(c))
        _dataBytesLiteral = ''.join(str( bytes(_dataByteArray), 'ISO-8859-1') )
        #print(c)
    else:
        if _packet_being_received == True:
            _dataByteArray.append(ord(c))
            _dataBytesLiteral = ''.join(str( bytes(_dataByteArray), 'ISO-8859-1') )
            #print(c)

def inicbuff():
    #self._serialport.flushInput()
    _dataByteArray.clear()
    _dataBytesLiteral = b''

def handle_data(c):
    addcbuff(c)

def process_data():
    #print("process")
    _msgwasreceived = True
    serial_cmd_result[0] = _dataByteArray.copy()
'''
while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()
