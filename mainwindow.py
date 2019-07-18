# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from datalistener import DataListener
from devicemainboard import BCmb

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 553)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 871, 411))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel { background-color : none; color : black; border: 3px solid black; }")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(470, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel { background-color : red; color : white; border: 1px solid black; }")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(90, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(280, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(470, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pbProgram1 = QtWidgets.QProgressBar(self.tab)
        self.pbProgram1.setGeometry(QtCore.QRect(90, 170, 141, 31))
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
        self.pbProgram1.setProperty("value", 24)
        self.pbProgram1.setObjectName("pbProgram1")
        self.pbProgram2 = QtWidgets.QProgressBar(self.tab)
        self.pbProgram2.setGeometry(QtCore.QRect(280, 170, 141, 31))
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
        self.pbProgram2.setProperty("value", 24)
        self.pbProgram2.setObjectName("pbProgram2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
        self.progressBar_3.setStyleSheet("QProgressBar\n"
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
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.cmdDisplay1 = QtWidgets.QPushButton(self.tab)
        self.cmdDisplay1.setGeometry(QtCore.QRect(90, 140, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdDisplay1.setFont(font)
        self.cmdDisplay1.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdDisplay1.setFlat(True)
        self.cmdDisplay1.setObjectName("cmdDisplay1")
        self.cmdIniciar1 = QtWidgets.QPushButton(self.tab)
        self.cmdIniciar1.setGeometry(QtCore.QRect(80, 220, 151, 32))
        self.cmdIniciar1.setObjectName("cmdIniciar1")
        self.cmdPausar1 = QtWidgets.QPushButton(self.tab)
        self.cmdPausar1.setGeometry(QtCore.QRect(80, 250, 151, 32))
        self.cmdPausar1.setObjectName("cmdPausar1")
        self.cmdDetener1 = QtWidgets.QPushButton(self.tab)
        self.cmdDetener1.setGeometry(QtCore.QRect(80, 280, 151, 32))
        self.cmdDetener1.setObjectName("cmdDetener1")
        self.cmdIniciar2 = QtWidgets.QPushButton(self.tab)
        self.cmdIniciar2.setGeometry(QtCore.QRect(270, 220, 151, 32))
        self.cmdIniciar2.setObjectName("cmdIniciar2")
        self.cmdPausar2 = QtWidgets.QPushButton(self.tab)
        self.cmdPausar2.setGeometry(QtCore.QRect(270, 250, 151, 32))
        self.cmdPausar2.setObjectName("cmdPausar2")
        self.cmdDetener2 = QtWidgets.QPushButton(self.tab)
        self.cmdDetener2.setGeometry(QtCore.QRect(270, 280, 151, 32))
        self.cmdDetener2.setObjectName("cmdDetener2")
        self.cmdDisplay2 = QtWidgets.QPushButton(self.tab)
        self.cmdDisplay2.setGeometry(QtCore.QRect(280, 140, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdDisplay2.setFont(font)
        self.cmdDisplay2.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdDisplay2.setFlat(True)
        self.cmdDisplay2.setObjectName("cmdDisplay2")
        self.cmdIniciarActualizar = QtWidgets.QPushButton(self.tab)
        self.cmdIniciarActualizar.setGeometry(QtCore.QRect(720, 80, 141, 32))
        self.cmdIniciarActualizar.setObjectName("cmdIniciarActualizar")
        self.cmdDetenerActualizar = QtWidgets.QPushButton(self.tab)
        self.cmdDetenerActualizar.setGeometry(QtCore.QRect(720, 110, 141, 32))
        self.cmdDetenerActualizar.setObjectName("cmdDetenerActualizar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.cmdConnect = QtWidgets.QPushButton(self.centralWidget)
        self.cmdConnect.setGeometry(QtCore.QRect(470, 10, 141, 32))
        self.cmdConnect.setObjectName("cmdConnect")
        self.cmdDisconnect = QtWidgets.QPushButton(self.centralWidget)
        self.cmdDisconnect.setGeometry(QtCore.QRect(610, 10, 141, 32))
        self.cmdDisconnect.setObjectName("cmdDisconnect")
        self.cmdForzarAtualizar = QtWidgets.QPushButton(self.centralWidget)
        self.cmdForzarAtualizar.setGeometry(QtCore.QRect(750, 10, 141, 32))
        self.cmdForzarAtualizar.setObjectName("cmdForzarAtualizar")
        self.txtHostname = QtWidgets.QTextEdit(self.centralWidget)
        self.txtHostname.setGeometry(QtCore.QRect(273, 20, 181, 21))
        self.txtHostname.setObjectName("txtHostname")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 902, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuVista = QtWidgets.QMenu(self.menuBar)
        self.menuVista.setObjectName("menuVista")
        self.menuCircuito = QtWidgets.QMenu(self.menuBar)
        self.menuCircuito.setObjectName("menuCircuito")
        self.menuHerramientas = QtWidgets.QMenu(self.menuBar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuReportes = QtWidgets.QMenu(self.menuBar)
        self.menuReportes.setObjectName("menuReportes")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionhh = QtWidgets.QAction(MainWindow)
        self.actionhh.setObjectName("actionhh")
        self.actionjjl = QtWidgets.QAction(MainWindow)
        self.actionjjl.setObjectName("actionjjl")
        self.actionhh_2 = QtWidgets.QAction(MainWindow)
        self.actionhh_2.setObjectName("actionhh_2")
        self.actionjjk = QtWidgets.QAction(MainWindow)
        self.actionjjk.setObjectName("actionjjk")
        self.actionjkjkj = QtWidgets.QAction(MainWindow)
        self.actionjkjkj.setObjectName("actionjkjkj")
        self.menuArchivo.addAction(self.actionhh)
        self.menuVista.addAction(self.actionjjl)
        self.menuCircuito.addAction(self.actionhh_2)
        self.menuHerramientas.addAction(self.actionjjk)
        self.menuReportes.addAction(self.actionjkjkj)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuVista.menuAction())
        self.menuBar.addAction(self.menuCircuito.menuAction())
        self.menuBar.addAction(self.menuHerramientas.menuAction())
        self.menuBar.addAction(self.menuReportes.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.showEvent = self.showEvent
        MainWindow.closeEvent = self.closeEvent

        self.cmdIniciar1.clicked.connect(self.on_cmdIniciar1_clicked)
        self.cmdIniciar2.clicked.connect(self.on_cmdIniciar2_clicked)

        self.cmdPausar1.clicked.connect(self.on_cmdPausar1_clicked)
        self.cmdPausar2.clicked.connect(self.on_cmdPausar2_clicked)

        self.cmdDetener1.clicked.connect(self.on_cmdDetener1_clicked)
        self.cmdDetener2.clicked.connect(self.on_cmdDetener2_clicked)

        self.cmdDisplay1.clicked.connect(self.on_cmdDisplay1_clicked)
        self.cmdDisplay2.clicked.connect(self.on_cmdDisplay2_clicked)

        self.cmdIniciarActualizar.clicked.connect(self.on_cmdIniciarActualizar_clicked)
        self.cmdDetenerActualizar.clicked.connect(self.on_cmdDetenerActualizar_clicked)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pantalla de Formación"))
        self.label.setText(_translate("MainWindow", "Mesa 1"))
        self.label_2.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
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
        self.label_4.setToolTip(_translate("MainWindow", "Thisis a tooltip"))
        self.label_4.setText(_translate("MainWindow", "Falla"))
        self.label_8.setText(_translate("MainWindow", "MF1"))
        self.label_9.setText(_translate("MainWindow", "MF2"))
        self.label_10.setText(_translate("MainWindow", "MF3"))
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
        self.cmdDisplay1.setText(_translate("MainWindow", "Voltage: 12.6V"))
        self.cmdIniciar1.setText(_translate("MainWindow", "Iniciar"))
        self.cmdPausar1.setText(_translate("MainWindow", "Pausar"))
        self.cmdDetener1.setText(_translate("MainWindow", "Detener"))
        self.cmdIniciar2.setText(_translate("MainWindow", "Iniciar"))
        self.cmdPausar2.setText(_translate("MainWindow", "Pausar"))
        self.cmdDetener2.setText(_translate("MainWindow", "Detener"))
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
        self.cmdDisplay2.setText(_translate("MainWindow", "Apagar"))
        self.cmdIniciarActualizar.setText(_translate("MainWindow", "Iniciar Actualizar"))
        self.cmdDetenerActualizar.setText(_translate("MainWindow", "Detener Actualizar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mesa 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mesa 2"))
        self.cmdConnect.setText(_translate("MainWindow", "Conectar"))
        self.cmdDisconnect.setText(_translate("MainWindow", "Desconectar"))
        self.cmdForzarAtualizar.setText(_translate("MainWindow", "Forzar Actualizar"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuVista.setTitle(_translate("MainWindow", "Vista"))
        self.menuCircuito.setTitle(_translate("MainWindow", "Circuito"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.actionhh.setText(_translate("MainWindow", "hh"))
        self.actionjjl.setText(_translate("MainWindow", "jjl"))
        self.actionhh_2.setText(_translate("MainWindow", "hh"))
        self.actionjjk.setText(_translate("MainWindow", "jjk"))
        self.actionjkjkj.setText(_translate("MainWindow", "jkjkj"))

    def showEvent(self, event):
        print("show")

    
    def closeEvent(self, event):
        print("close")

    def on_cmdIniciar1_clicked(self):
        print("Iniciar 1")
        BCmb.runClient('raspberrypi.local', 1)
    
    def on_cmdIniciar2_clicked(self):
        print("Iniciar 2")
        BCmb.runClient('raspberrypi.local', 2)
    

    def on_cmdPausar1_clicked(self):
        print("Pausar 1")
        BCmb.pauseClient('raspberrypi.local', 1)
    
    def on_cmdPausar2_clicked(self):
        print("Pausar 2")
        BCmb.pauseClient('raspberrypi.local', 2)

    def on_cmdDetener1_clicked(self):
        print("Detener 1")
        BCmb.stopClient('raspberrypi.local', 1)
    
    def on_cmdDetener2_clicked(self):
        print("Detener 2")
        BCmb.stopClient('raspberrypi.local', 2)

    def on_cmdDisplay1_clicked(self):
        print("Display 1")
    
    def on_cmdDisplay2_clicked(self):
        print("Display 2")

    def testsCallback(self, msg):
        if "DataListener[True]" in msg:
            msg = msg.replace("DataListener[True]:","")
            #newstr = msg.split(',')
            newstr = msg
            print (newstr)
            self.cmdDisplay1.setText(str(newstr))
            self.cmdDisplay1.repaint()
            self.cmdDisplay1.update()
            self.cmdDisplay1.setUpdatesEnabled(True)

    def on_cmdIniciarActualizar_clicked(self):
        print("Iniciar Actualizar")
        self.dataThread = DataListener(self.testsCallback)
        self.dataThread.start()

    def on_cmdDetenerActualizar_clicked(self):
        print("Detener Actualizar")
        self.dataThread.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



