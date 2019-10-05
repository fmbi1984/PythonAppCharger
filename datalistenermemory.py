from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
import appsettings

from devicemainboard import BCmb
from report import IndividualReport

logger = logging.getLogger(__name__)


class ACTION(Enum):
    PASS = 0
    FAIL = 1


class DataListenerMemory(Thread):

    mySrc = None
    _stop_event = None

    def __init__(self, args):
        '''Constructor'''
        Thread.__init__(self)
        self._args = args
        self._name = "DataListenerServer Thread"
        if args != None:
            self.mySrc = Communicate()
            self.mySrc.myGUI_signal.connect(args)

        self._stop_event = Event()
        self._stop_event.clear()

    def run(self):
        # try:
        print(self._name+" started")
        self.pingForDevicesPresent()
        # while not self._stop_event.is_set():
        if BCmb.memoryDataClient('raspberrypi.local', 1) == False:
            print("False")
        else:
            print("True")
		# we do ping to the devices
        sleep(.1)
        print(self._name+" stopped")
        

    def stop(self):
        print("stop was done in "+self._name)
        self._stop_event.set()

    def join(self, *args, **kwargs):
        self.stop()
        super(DataListenerMemory,self).join(*args, **kwargs)

    def pingForDevicesPresent(self):
        # we do ping to the devices 
 
        for i in range(shared.devStart, shared.devStop+1):
            address=i
            print("Doing ping to device No."+str(address))
            readData = BCmb.ping(address)
            print("VALUE:")
            print(str(readData))
            shared.DEV[i][0] = False
            if readData!= None:
                if readData == True:
                    shared.DEV[i][0] = True
                    print("DEV"+str(address)+" is Present!")  
                else:
                    print("DEV"+str(address)+" is not Present!")
                    # ireport.end()
            else:
                print("DEV"+str(address)+" is not Present!")
                # ireport.end()

if __name__ == '__main__':
    # logger.debug("demo")
    print("Demo")
    main = DataListenerMemory(None)
    # main.daemon = True
    main.start()
    # main.stop()
