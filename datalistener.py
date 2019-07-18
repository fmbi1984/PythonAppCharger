from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging

from communicate import Communicate
import shared
import appsettings

from devicemainboard import BCmb

logger = logging.getLogger(__name__)

class DataListener(Thread):


    mySrc = None

    _stop_event = None


    def __init__(self, args):
        '''Constructor'''
        Thread.__init__(self)
        self._args = args
        self._name = "DataListener Thread"
        if args != None:
            self.mySrc = Communicate()
            self.mySrc.myGUI_signal.connect(args)
        
        self._stop_event = Event()
        self._stop_event.clear()
        
    def run(self):

        print(self._name+" started")
        number=0
        while not self._stop_event.is_set():
            #1.read data
            #BCmb.readDataClient('raspberrypi.local', 1)
            #BCmb.readDataClient('raspberrypi.local', 2)
            
            #2.parse string to update UI

            #3.send to UI
            number = number + 1
            self.dataStr = str(number)
            #print(self.dataStr)
            if self.mySrc != None:
                self.mySrc.myGUI_signal.emit("DataListener[True]:"+self.dataStr)
            sleep(.1)
        print(self._name+" stopped")
           

    def stop(self):
        self._stop_event.set()

    def join(self, *args, **kwargs):
        self.stop()
        super(DataListener,self).join(*args, **kwargs)

if __name__ == '__main__':
    logger.debug("demo")
    main = DataListener(None)
    #main.daemon = True
    main.start()
    #main.stop()