# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1800, 1156)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphWidget_time = PlotWidget(self.centralwidget)
        self.graphWidget_time.setObjectName(u"graphWidget_time")
        self.graphWidget_time.setGeometry(QRect(20, 500, 1751, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget_time.sizePolicy().hasHeightForWidth())
        self.graphWidget_time.setSizePolicy(sizePolicy)
        self.graphWidget_FFT = PlotWidget(self.centralwidget)
        self.graphWidget_FFT.setObjectName(u"graphWidget_FFT")
        self.graphWidget_FFT.setGeometry(QRect(20, 30, 1221, 441))
        sizePolicy.setHeightForWidth(self.graphWidget_FFT.sizePolicy().hasHeightForWidth())
        self.graphWidget_FFT.setSizePolicy(sizePolicy)
        self.graphWidget_constellation = PlotWidget(self.centralwidget)
        self.graphWidget_constellation.setObjectName(u"graphWidget_constellation")
        self.graphWidget_constellation.setGeometry(QRect(1260, 30, 511, 441))
        sizePolicy.setHeightForWidth(self.graphWidget_constellation.sizePolicy().hasHeightForWidth())
        self.graphWidget_constellation.setSizePolicy(sizePolicy)
        self.tableWidget_receive = QTableWidget(self.centralwidget)
        self.tableWidget_receive.setObjectName(u"tableWidget_receive")
        self.tableWidget_receive.setGeometry(QRect(930, 750, 841, 361))
        self.tableWidget_send = QTableWidget(self.centralwidget)
        self.tableWidget_send.setObjectName(u"tableWidget_send")
        self.tableWidget_send.setGeometry(QRect(20, 750, 881, 361))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1260, 10, 81, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 81, 17))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 480, 81, 17))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 730, 81, 17))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(930, 730, 81, 17))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Constellation", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FFT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time signal", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Log Send", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Log Receive", None))
    # retranslateUi

