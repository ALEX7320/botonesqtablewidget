# modulos de PySide2 utilizados
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2.QtWidgets import QHeaderView

# importar diseño
from view.ui_VentanaTabla import Ui_VentanaTabla

# import acciones de la tabla
from accionestabla import Clase_AccionTabla

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        self.raiz = Ui_VentanaTabla()
        self.raiz.setupUi(self)

        # las acciones a realizar con la tabla
        self.tablaconfig = Clase_AccionTabla()

        # columnas elasticas de la tabla
        self.raiz.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # nuestro registro de datos
        datolista=[
                ['A1','Valeria','valeria@gmail.com','25'],
                ['A2','Jeronima','jeronima@gmail.com','35'],
                ['A3','Santiago','santiago@gmail.com','78'],
                ['A4','Javier','javier@gmail.com','58'],
                ['A5','Thomas','thomas@gmail.com','25'],
                ['A6','Pedro','pedro@gmail.com','42'],
                ]

        # vaciar tabla
        self.raiz.btn_vaciar.clicked.connect(lambda : self.raiz.tabla.setRowCount(0))
        
        # llenar la tabla
        self.raiz.btn_actualizar.clicked.connect(lambda : 
            self.tablaconfig.llenadoTabla(self.raiz.tabla,datolista)
            )
        

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
