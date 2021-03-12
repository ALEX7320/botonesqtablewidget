# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_VentanaTablaUfajmC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaTabla(object):
    def setupUi(self, VentanaTabla):
        if not VentanaTabla.objectName():
            VentanaTabla.setObjectName(u"VentanaTabla")
        VentanaTabla.resize(719, 343)
        VentanaTabla.setFocusPolicy(Qt.ClickFocus)
        self.centralwidget = QWidget(VentanaTabla)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_actualizar = QPushButton(self.centralwidget)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(450, 280, 111, 41))
        self.btn_vaciar = QPushButton(self.centralwidget)
        self.btn_vaciar.setObjectName(u"btn_vaciar")
        self.btn_vaciar.setGeometry(QRect(580, 280, 111, 41))
        self.tabla = QTableWidget(self.centralwidget)
        if (self.tabla.columnCount() < 5):
            self.tabla.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(30, 30, 661, 231))
        self.tabla.setStyleSheet(u"")
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla.horizontalHeader().setHighlightSections(False)
        self.tabla.verticalHeader().setVisible(False)
        VentanaTabla.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaTabla)

        QMetaObject.connectSlotsByName(VentanaTabla)
    # setupUi

    def retranslateUi(self, VentanaTabla):
        VentanaTabla.setWindowTitle(QCoreApplication.translate("VentanaTabla", u"Botones en tabla - ALEX7320", None))
        self.btn_actualizar.setText(QCoreApplication.translate("VentanaTabla", u"Actualizar", None))
        self.btn_vaciar.setText(QCoreApplication.translate("VentanaTabla", u"Vaciar", None))
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaTabla", u"ID", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaTabla", u"Usuario", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaTabla", u"Correo", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaTabla", u"Edad", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaTabla", u"Acciones", None));
    # retranslateUi

