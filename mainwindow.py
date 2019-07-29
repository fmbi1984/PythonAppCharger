# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt, pyqtSlot 
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from time import sleep
from datalistener import DataListener
from devicemainboard import BCmb
import shared
import time
import threading
from datetime import timedelta

import glob, os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 553)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 851, 421))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.cmdType2 = QtWidgets.QPushButton(self.tab)
        self.cmdType2.setGeometry(QtCore.QRect(360, 220, 41, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdType2.setFont(font)
        self.cmdType2.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdType2.setText("")
        self.cmdType2.setFlat(True)
        self.cmdType2.setObjectName("cmdType2")
        self.pbProgram2 = QtWidgets.QProgressBar(self.tab)
        self.pbProgram2.setGeometry(QtCore.QRect(240, 190, 161, 31))
        self.pbProgram2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
        self.pbProgram2.setProperty("value", 0)
        self.pbProgram2.setObjectName("pbProgram2")
        self.cmdDisplay1 = QtWidgets.QPushButton(self.tab)
        self.cmdDisplay1.setGeometry(QtCore.QRect(50, 130, 161, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdDisplay1.setFont(font)
        self.cmdDisplay1.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdDisplay1.setFlat(True)
        self.cmdDisplay1.setObjectName("cmdDisplay1")
        self.lblTab1 = QtWidgets.QLabel(self.tab)
        self.lblTab1.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lblTab1.setFont(font)
        self.lblTab1.setObjectName("lblTab1")
        self.chk2 = QtWidgets.QCheckBox(self.tab)
        self.chk2.setGeometry(QtCore.QRect(240, 110, 86, 20))
        self.chk2.setText("")
        self.chk2.setObjectName("chk2")
        self.cbProgram2 = QtWidgets.QComboBox(self.tab)
        self.cbProgram2.setGeometry(QtCore.QRect(240, 160, 161, 32))
        self.cbProgram2.setStyleSheet("QComboBox { background-color : white; color : black; border: 1px solid black; }")
        self.cbProgram2.setObjectName("cbProgram2")
        self.pbProgram1 = QtWidgets.QProgressBar(self.tab)
        self.pbProgram1.setGeometry(QtCore.QRect(50, 190, 161, 31))
        self.pbProgram1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
        self.pbProgram1.setProperty("value", 0)
        self.pbProgram1.setObjectName("pbProgram1")
        self.chk1 = QtWidgets.QCheckBox(self.tab)
        self.chk1.setGeometry(QtCore.QRect(50, 110, 86, 20))
        self.chk1.setText("")
        self.chk1.setObjectName("chk1")
        self.cbProgram1 = QtWidgets.QComboBox(self.tab)
        self.cbProgram1.setGeometry(QtCore.QRect(50, 160, 161, 32))
        self.cbProgram1.setStyleSheet("QComboBox { background-color : white; color : black; border: 1px solid black; }")
        self.cbProgram1.setObjectName("cbProgram1")
        self.cmdStatus1 = QtWidgets.QPushButton(self.tab)
        self.cmdStatus1.setGeometry(QtCore.QRect(50, 220, 121, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdStatus1.setFont(font)
        self.cmdStatus1.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdStatus1.setText("")
        self.cmdStatus1.setFlat(True)
        self.cmdStatus1.setObjectName("cmdStatus1")
        self.cmdDisplay2 = QtWidgets.QPushButton(self.tab)
        self.cmdDisplay2.setGeometry(QtCore.QRect(240, 130, 161, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdDisplay2.setFont(font)
        self.cmdDisplay2.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdDisplay2.setFlat(True)
        self.cmdDisplay2.setObjectName("cmdDisplay2")
        self.lblDevice1 = QtWidgets.QLabel(self.tab)
        self.lblDevice1.setGeometry(QtCore.QRect(70, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lblDevice1.setFont(font)
        self.lblDevice1.setObjectName("lblDevice1")
        self.lblDevice2 = QtWidgets.QLabel(self.tab)
        self.lblDevice2.setGeometry(QtCore.QRect(260, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lblDevice2.setFont(font)
        self.lblDevice2.setObjectName("lblDevice2")
        self.cmdStatus2 = QtWidgets.QPushButton(self.tab)
        self.cmdStatus2.setGeometry(QtCore.QRect(240, 220, 121, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdStatus2.setFont(font)
        self.cmdStatus2.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdStatus2.setText("")
        self.cmdStatus2.setFlat(True)
        self.cmdStatus2.setObjectName("cmdStatus2")
        self.cmdType1 = QtWidgets.QPushButton(self.tab)
        self.cmdType1.setGeometry(QtCore.QRect(170, 220, 41, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdType1.setFont(font)
        self.cmdType1.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdType1.setText("")
        self.cmdType1.setFlat(True)
        self.cmdType1.setObjectName("cmdType1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.cmdSelect = QtWidgets.QPushButton(self.centralWidget)
        self.cmdSelect.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.cmdSelect.setObjectName("cmdSelect")
        self.cmdStart = QtWidgets.QPushButton(self.centralWidget)
        self.cmdStart.setGeometry(QtCore.QRect(180, 10, 171, 41))
        self.cmdStart.setObjectName("cmdStart")
        self.cmdStop = QtWidgets.QPushButton(self.centralWidget)
        self.cmdStop.setGeometry(QtCore.QRect(520, 10, 171, 41))
        self.cmdStop.setObjectName("cmdStop")
        self.cmdPause = QtWidgets.QPushButton(self.centralWidget)
        self.cmdPause.setGeometry(QtCore.QRect(350, 10, 171, 41))
        self.cmdPause.setObjectName("cmdPause")
        self.cmdUpdate = QtWidgets.QPushButton(self.centralWidget)
        self.cmdUpdate.setGeometry(QtCore.QRect(690, 10, 171, 41))
        self.cmdUpdate.setObjectName("cmdUpdate")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 902, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menuBar)
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.menuArchivo.addAction(self.exit)
        self.menuBar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.MainWindow = MainWindow

        MainWindow.showEvent = self.showEvent
        MainWindow.closeEvent = self.closeEvent

        self.cmdStart.clicked.connect(self.on_cmdStart_clicked)

        self.cmdPause.clicked.connect(self.on_cmdPause_clicked)

        self.cmdStop.clicked.connect(self.on_cmdStop_clicked)

        self.cmdDisplay1.clicked.connect(self.on_cmdDisplay_clicked)
        self.cmdDisplay2.clicked.connect(self.on_cmdDisplay_clicked)

        #self.cmdUpdate.clicked.connect(self.on_cmdUpdate_clicked)
        #self.cmdDetenerActualizar.clicked.connect(self.on_cmdDetenerActualizar_clicked)

        self.cmdSelect.clicked.connect(self.on_cmdGroup_clicked)
        
        self.cmdDisplay1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.cmdDisplay2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        
        start_action1 = QAction("Iniciar", self.cmdDisplay1)
        pause_action1 = QAction("Pausar", self.cmdDisplay1)
        stop_action1 = QAction("Detener", self.cmdDisplay1)

        start_action2 = QAction("Iniciar", self.cmdDisplay2)
        pause_action2 = QAction("Pausar", self.cmdDisplay2)
        stop_action2 = QAction("Detener", self.cmdDisplay2)

        start_action1.triggered.connect(self.__start)
        pause_action1.triggered.connect(self.__pause)
        stop_action1.triggered.connect(self.__stop)

        start_action2.triggered.connect(self.__start)
        pause_action2.triggered.connect(self.__pause)
        stop_action2.triggered.connect(self.__stop)
        
        self.cmdDisplay1.addAction(start_action1)
        self.cmdDisplay1.addAction(pause_action1)
        self.cmdDisplay1.addAction(stop_action1)

        self.cmdDisplay2.addAction(start_action2)
        self.cmdDisplay2.addAction(pause_action2)
        self.cmdDisplay2.addAction(stop_action2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pantalla de Formación"))
        self.cmdType2.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.pbProgram2.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.cmdDisplay1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.cmdDisplay1.setText(_translate("MainWindow", "0.0 V"))
        self.lblTab1.setText(_translate("MainWindow", "Mesa 1"))
        self.pbProgram1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.cmdStatus1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.cmdDisplay2.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.cmdDisplay2.setText(_translate("MainWindow", "0.0 V"))
        self.lblDevice1.setText(_translate("MainWindow", "MF1"))
        self.lblDevice2.setText(_translate("MainWindow", "MF2"))
        self.cmdStatus2.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.cmdType1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mesa 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mesa 2"))
        self.cmdSelect.setText(_translate("MainWindow", "Seleccionar"))
        self.cmdStart.setText(_translate("MainWindow", "Iniciar"))
        self.cmdStop.setText(_translate("MainWindow", "Stop"))
        self.cmdPause.setText(_translate("MainWindow", "Pausar"))
        self.cmdUpdate.setText(_translate("MainWindow", "Forzar Actualizar"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.exit.setText(_translate("MainWindow", "Salir"))


    hostname = 'raspberrypi.local'

    def display(self):
        print(time.ctime())

        for index in range(1,4):
            if shared.DEV[index][0] == True:
                newstr1 = ""
                if shared.DEV[index][9] == 1:
                    #current
                    newstr1 = str(shared.DEV[index][1])+" A"
                if shared.DEV[index][9] == 2:
                    #voltage
                    newstr1 = str(shared.DEV[index][2]) + " V"
                if shared.DEV[index][9] == 3:
                    #temperature
                    newstr1 = str(shared.DEV[index][3]) + " °C"
                
                cmdDisplay = getattr(self, "cmdDisplay"+str(index))
                cmdDisplay.setText(str(newstr1))
                
                
                pbObj = getattr(self, "pbProgram"+str(index))
                if float(shared.DEV[index][6]) > 0:
                    percentage = (100/float(shared.DEV[index][6])) * float(shared.DEV[index][5])
                    pbObj.setValue(percentage)
                else:
                    pbObj.setValue(0)
                
                cmdDisplay.repaint()
                cmdDisplay.update()
                cmdDisplay.setUpdatesEnabled(True)

                pbObj.repaint()
                pbObj.update()
                pbObj.setUpdatesEnabled(True)
            #else:
            #    print("ERROR PING")

    def tick(self):
        #print("tick")
        #we update here our controls
        self.display()

    def callback(self):
        print("display")

    def showEvent(self, event):
        print("show")
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.setInterval(1000)
        self.timer.start() 
        #self.display()
        #self.unitializeCheckbox()
        self.updateThread = DataListener(self.callback)
        self.updateThread.start()
        self.fillProgramComboBoxes()
        

    def closeEvent(self, event):
        print("close")
        self.updateThread.stop()

    def fillProgramComboBoxes(self):
        oldpwd=os.getcwd()
        os.chdir("FormationDataFiles")
        fileList = []
        for fileName in glob.glob("*.json"):
            fileList.append(fileName)
            #print(fileName)
        fileList.sort()
        print(fileList)
        os.chdir(oldpwd)

        for elem in fileList:
            self.cbProgram1.addItem(str(elem))
            self.cbProgram2.addItem(str(elem))


    def unitializeCheckbox(self):
        self.chk1.setVisible(False)
        self.chk1.setCheckState(QtCore.Qt.Unchecked)

        self.chk2.setVisible(False)
        self.chk2.setCheckState(QtCore.Qt.Unchecked)

    def initializeCheckbox(self):
        self.chk1.setVisible(True)
        self.chk1.setCheckState(QtCore.Qt.Unchecked)

        self.chk2.setVisible(True)
        self.chk2.setCheckState(QtCore.Qt.Unchecked)

    def on_cmdGroup_clicked(self):  
        self.initializeCheckbox()
    
    def remove_char(self, input_string, index):
        first_part = input_string[:index]
        second_part = input_string[index+1:]
        return first_part + second_part

    def prepare_toSend(self, dataOrig):
        #print(dataOrig)
        data2 = str(dataOrig).replace("{\"steps\": ", '')
        #print(data2)
        value_index = len(data2)-1
        data3 = self.remove_char(data2, value_index)
        #print(data3)
        return data3

    def on_cmdStart_clicked(self):
        if self.chk1.isChecked:
            print("Iniciar 1")
            BCmb.runClient(self.hostname, 1)
        if self.chk2.isChecked:
            print("Iniciar 2")
            BCmb.runClient(self.hostname, 2)
        self.unitializeCheckbox()
    
    def on_cmdPause_clicked(self):
        if self.chk1.isChecked:
            print("Pausar 1")
            BCmb.pauseClient(self.hostname, 1)
        if self.chk2.isChecked:
            print("Pausar 2")
            BCmb.pauseClient(self.hostname, 2)
        self.unitializeCheckbox()
    

    def on_cmdStop_clicked(self):
        
        if self.chk1.isChecked:
            print("Detener 1")
            BCmb.stopClient(self.hostname, 1)
        if self.chk2.isChecked:
            print("Detener 2")
            BCmb.stopClient(self.hostname, 2)

        self.unitializeCheckbox()

    def on_cmdDisplay_clicked(self):
        temp = self.MainWindow.sender().objectName()
        temp2 = temp.replace("cmdDisplay", "")
        print("Display "+temp2)
        nDev = int(temp2)

        shared.DEV[nDev][9] = shared.DEV[nDev][9] + 1
        if shared.DEV[nDev][9]==4 :
            shared.DEV[nDev][9] = 1
        print(shared.DEV[nDev][9])

    def __start(self):
        print("Start")
        senderName = self.MainWindow.sender().parent().objectName()
        nStrDevice = senderName.replace("cmdDisplay", "")
        print("Display "+nStrDevice)
        self.updateThread.stop()
        sleep(.5)
        cbxPgr = getattr(self, "cbProgram"+nStrDevice)
        programName = cbxPgr.currentText()

        f= open("FormationDataFiles/"+programName,"r")
        contents = f.read()
        f.close()

        program = self.prepare_toSend(contents)

        BCmb.writeProgramClient(self.hostname,int(nStrDevice), program)
        
        sleep(3)
        BCmb.runClient(self.hostname, int(nStrDevice))
        sleep(.5)
        self.updateThread = DataListener(self.callback)
        self.updateThread.start()

    def __pause(self):
        print("Pause")
        senderName = self.MainWindow.sender().parent().objectName()
        nStrDevice = senderName.replace("cmdDisplay", "")
        print("Display "+nStrDevice)
        self.updateThread.stop()
        sleep(.5)
        BCmb.pauseClient(self.hostname, int(nStrDevice))
        sleep(.5)
        self.updateThread = DataListener(self.callback)
        self.updateThread.start()

    def __stop(self):
        print("Stop")
        senderName = self.MainWindow.sender().parent().objectName()
        nStrDevice = senderName.replace("cmdDisplay", "")
        print("Display "+nStrDevice)
        self.updateThread.stop()
        sleep(.5)
        BCmb.stopClient(self.hostname, int(nStrDevice))
        sleep(.5)
        self.updateThread = DataListener(self.callback)
        self.updateThread.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

