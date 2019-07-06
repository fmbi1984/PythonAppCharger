import logging
from time import sleep, time

import StringUtils

import os
import sys
import subprocess
import shared
import math
from enum import Enum

import shared
import appsettings

from devinterface import devInterface

from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QScrollBar
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QDesktopServices
from PyQt5.QtCore import QEventLoop, QByteArray, Qt, QUrl, pyqtSignal, pyqtSlot, QObject, QTimer

logger = logging.getLogger(__name__)

class ACTION(Enum):
    PASS = 0
    FAIL = 1

class BCmb(object):
    timeout = 10
    attempts = 1

    @staticmethod
    def writeProgramClient(hostname,addr, program_in_json):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x57, program_in_json, BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    @staticmethod
    def runClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x33, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    @staticmethod
    def pauseClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x34, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result
    
    @staticmethod
    def stopClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x35, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    @staticmethod
    def readProgramClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x52, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result
    '''
    @staticmethod
    def readVoltageClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x56, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    @staticmethod
    def readTemperatureClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x54, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    @staticmethod
    def readCurrentClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x49, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result
    
    @staticmethod
    def readDataClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendCommandAndGetResponse(addr, 0x43, "", 0.25)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result
    '''

    @staticmethod
    def readStepClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x50, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result
    '''
    @staticmethod
    def readTypeClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x50, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result
    '''

    @staticmethod
    def currentTimeClient(hostname,addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x74, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    @staticmethod
    def setAddress(address):
        result = ACTION.FAIL
        result = devInterface.sendCommandAndGetResponse(None, 0xFF, str(chr(address)), BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    @staticmethod
    def getAddress():
        result = ACTION.FAIL
        result = devInterface.sendCommandAndGetResponse(None, 0xFF, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result

    '''
    @staticmethod
    def writeProgramFake(addr, program_in_json):
        result = ACTION.FAIL
        result = devInterface.sendCommandAndGetResponseFake(addr, 0x57, program_in_json, BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result
    '''

    @staticmethod
    def readDataClient(hostname, addr):
        result = ACTION.FAIL
        result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x43, "", BCmb.timeout)
        print(result)
        if result != None:
            if result[1] == 'PASS':
                result = ACTION.PASS
            else:
                result = ACTION.FAIL
        return result


if __name__ == "__main__":
    print("tests")
    #BCmb.writeProgram(0, "[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"10000\"},{\"Type\":\"Charge\",\"Time\":\"120000\",\"Current\":\"8.0\"},{\"Type\":\"Charge\",\"Time\":\"50000\",\"Current\":\"12.0\"},{\"Type\":\"Carga\",\"Time\":\"60000\",\"Current\":\"15.0\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"20.0\"},{\"Type\":\"Pause\",\"Time\":\"20000\"},{\"Type\":\"Charge\",\"Time\":\"30000\",\"Current\":\"10.5\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"14.5\"},{\"Type\":\"End\"}]")
    #BCmb.readProgram(0)
    #BCmb.setAddress(1)
    #BCmb.run(1)
    #BCmb.stop(1)
    #BCmb.readStep(0)
    #BCmb.currentTime(0)
    #BCmb.readProgram(0)
    #BCmb.readDataClient('raspberrypi.local', 1)
    
    #BCmb.stop(1)
    #BCmb.readData(2)
    '''
    BCmb.getAddress()
    BCmb.readProgram(2)
    BCmb.run(2)
    '''

    #BCmb.runClient('raspberrypi.local', 2)
    #BCmb.pauseClient('raspberrypi.local', 2)
    #BCmb.stopClient('raspberrypi.local', 2)
    #BCmb.readStepClient('raspberrypi.local', 2)
    #BCmb.currentTimeClient('raspberrypi.local', 2)
    #BCmb.readProgramClient('raspberrypi.local', 2)
    #BCmb.writeProgramClient('raspberrypi.local',2,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"10000\"},{\"Type\":\"Charge\",\"Time\":\"120000\",\"Current\":\"8.0\"},{\"Type\":\"Charge\",\"Time\":\"50000\",\"Current\":\"12.0\"},{\"Type\":\"Carga\",\"Time\":\"60000\",\"Current\":\"15.0\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"20.0\"},{\"Type\":\"Pause\",\"Time\":\"20000\"},{\"Type\":\"Charge\",\"Time\":\"30000\",\"Current\":\"10.5\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"14.5\"},{\"Type\":\"End\"}]")

    
    '''
    while True:
        #BCmb.readData(1)
        BCmb.readDataClient('raspberrypi.local', 1)
        BCmb.readDataClient('raspberrypi.local', 2)
        sleep(.1)
    '''
