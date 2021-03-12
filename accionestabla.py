# modulos de PySide2 utilizados
from PySide2.QtWidgets import QHBoxLayout,QPushButton,QWidget,QTableWidgetItem,QSizePolicy
from PySide2.QtCore import Qt,QSize,QCoreApplication
from PySide2.QtGui import QIcon

class Clase_AccionTabla():

    def __init__(self):
        pass
    
    # CREACION DE BOTONE *-*-*-*-*-*-*-*-*

    def creabotones(self, estilo=None, titulo=None, icono=None, tooltip=None):

        # configuraciones generales
        boton_nuevo = QPushButton()
        boton_nuevo.setStyleSheet(estilo)
        boton_nuevo.setIcon(QIcon(icono)) 
        boton_nuevo.setToolTip(tooltip)
        boton_nuevo.setText(titulo)

        # configuracion de resize
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(boton_nuevo.sizePolicy().hasHeightForWidth())
        boton_nuevo.setSizePolicy(sizePolicy)

        return boton_nuevo

    #LLENADO DE TABLA *-*-*-*-*-*-*-*-*

    def llenadoTabla(self,tabla,lista):
        '''llenado de datos a la tabla'''

        # vaciar QTableWidget
        tabla.setRowCount(0)

        # crea numero de filas con respecto a la lista
        # de elementos
        tabla.setRowCount(len(lista))

        # RECORRER COLUMNAS Y LISTA DE ITEMS /*/*/*/*/*/*/*/*/*/*/*/*/*/
        for fila,listaItem in enumerate(lista):
            """
            fila = cantidad de listas de la lista
            listaItem = lista que contiene valores
            """

            # CREAR BOTONES /*/*/*/*/*/*/*/*/*/*/*/*/*/
            btn_uno = self.creabotones(
                estilo = (u"""
                          QPushButton{background-color: #52CF33; color: white}
                          QPushButton:hover{background-color: #32EF03}
                          QPushButton:pressed{background-color: #43A02C}"""),
                icono = 'icons/edit.png',
                titulo = u' Editar',
                tooltip = 'Editar')

            btn_dos = self.creabotones(
                estilo = (u"""
                          QPushButton{background-color: #DB224F; color: white}
                          QPushButton:hover{background-color: #F41E52}
                          QPushButton:pressed{background-color: #A91E40}"""),
                icono = 'icons/delete.png',
                titulo = u'Eliminar',
                tooltip = 'Eliminar')           

            # AGRUPAR BOTONES /*/*/*/*/*/*/*/*/*/*/*/*/*/
            layout = QHBoxLayout()
            layout.setContentsMargins(0,0,0,0) # espaciado
            layout.setSpacing(0) # espaciado
            layout.addWidget(btn_uno) # agregar botones al layout
            layout.addWidget(btn_dos)
            widget = QWidget()
            widget.setLayout(layout)
            # widget de botones en la columna final 
            tabla.setCellWidget(fila ,tabla.columnCount()-1,widget)

            # SINCRONIZAR ACCIONES /*/*/*/*/*/*/*/*/*/*/*/*/*/
            self.boton_uno_coneccion(btn_uno, fila, tabla, listaItem)
            self.boton_dos_connecion(btn_dos, fila, tabla, listaItem)

            # AGREGAR ITEMS /*/*/*/*/*/*/*/*/*/*/*/*/*/
            for columna,item in enumerate(listaItem):
                """
                cantidad de elmentos de la lista = columna
                valor de la lista = item
                """

                tabla.setItem(fila, columna, QTableWidgetItem(str(item))) # insertar items
                tabla.item(fila,columna).setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter) # alinear items


    #SINCRONIZAR ACCIONES *-*-*-*-*-*-*-*-*

    def boton_uno_coneccion(self, b_uno, fila, tabla, listaval):
        """boton uno"""

        # selecciona fila (pinta)
        b_uno.clicked.connect(lambda:tabla.selectRow(fila))

        # acciones a realizar
        b_uno.clicked.connect(lambda: 
            self.boton_uno_accion(tabla.item(fila, 0).text(), # id
            listaval)) # elementos

    def boton_dos_connecion(self, b_dos, fila, tabla, listaval):
        """boton dos"""

        # selecciona fila (pinta)
        b_dos.clicked.connect(lambda:tabla.selectRow(fila)) 

        # acciones a realizar
        b_dos.clicked.connect(lambda: 
            self.boton_dos_accion(tabla.item(fila, 0).text(), # id
            listaval)) # elmentos


    #ASIGNAR ACCIONES *-*-*-*-*-*-*-*-*

    def boton_uno_accion(self, ide, elementos):
        """todas las acciones del boton"""
        # EDITAR
        
        print(f'Editar ID: {ide}') # acciona a realizar
        print(f'Editar Elementos: {elementos}') # acciona a realizar


    def boton_dos_accion(self,ide, elementos):
        """todas las acciones del boton"""
        # ELIMINAR

        print(f'Eliminar ID: {ide}') # acciona a realizar
        print(f'Eliminar Elementos: {elementos}') # acciona a realizar

