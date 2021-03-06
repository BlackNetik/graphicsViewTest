# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from pyqtgraph import PlotWidget
import numpy as np
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 400, 751, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        #Установка graphicsView
        self.graphicsView = PlotWidget(self.centralwidget)
        #Установка размера и позиции
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 761, 361))
        self.graphicsView.setObjectName("graphicsView")
        #Установка цвета
        self.graphicsView.setBackground((100,50,255,25))
        #Название графика
        self.graphicsView.setTitle("График посещаемости")
        #Показ осей X и Y
        self.graphicsView.showGrid(x=True, y=True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Три кнопки и их реакции при нажатии
        self.pushButton.clicked.connect(self.draw)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.zapoln)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test"))
        MainWindow.setWindowIcon(QtGui.QIcon('123.jpg'))
        self.pushButton.setText(_translate("MainWindow", "First"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "Second"))

    #Функция построения 100 точек, позиции которых определяются через рандомайзер
    def draw(self):
        self.graphicsView.clear()
        x = np.random.normal(size=100)
        y = np.random.normal(size=(3, 100))
        for i in range(3):
            self.graphicsView.plot(x, y[i], pen=(i, 3))

    #Очистка
    def clear(self):
        self.graphicsView.clear()

    #Заполнение графика заранее известными позициями. Две перпендикулярные линии
    def zapoln(self):
        self.graphicsView.clear()
        self.graphicsView.plot([1, 2, 3, 4, 5],[10, 15, 20, 25, 30], pen = 'r')
        self.graphicsView.plot([5, 4, 3, 2, 1], [10, 15, 20, 25, 30], pen='b')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
