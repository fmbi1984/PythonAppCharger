import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QScrollBar, QApplication, QWidget, QMainWindow
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QDesktopServices
from PyQt5.QtCore import QEventLoop, QByteArray, Qt, QUrl, pyqtSignal, pyqtSlot, QObject, QTimer, QElapsedTimer, QTime

serial_number = None

# constants that will indicate a pin state
LOW = 0
HIGH = 1

lock = threading.Lock() # lock will be used as a lock for the UART
ljLock = threading.Lock() # lock will be used as a lock for the labjack

devStart = 1
devStop = 1

DEV = [
    [False, 0, 0, 0, '', 0, 0, 0],
    [False, 0, 0, 0, '', 0, 0, 0],
    [False, 0, 0, 0, '', 0, 0, 0]
]



def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def dec2str(number, places):
    return '{:.2f}'.format(number)

def CenterWidgets(widget:QWidget):
    screenGeometry =  QApplication.desktop().screenGeometry()
    x = (screenGeometry.width() - widget.width())/ 2
    y = (screenGeometry.height()- widget.height())/ 2
    widget.move(x, y)

