# Agregar botones en QTableWidget

**Indice**
  * [Recursos utilizados](#recursos-utilizados)
  * [Acciones](#acciones)
  * [Inserción de datos](#inserción-de-datos)
  * [Diseño](#diseño)
  * [Previsualización](#previsualización)

# Recursos utilizados

`pip install PySide2`

# Acciones
En las funciones `boton_uno_accion` y `boton_dos_accion` del modulo `accionestabla.py` se colocara la funcionalidad que realizara dicho boton.
```python
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
```
# Inserción de datos
Esto se lleva a cabo mediante siguiente formato, teniendo en cuenta la ubicación de cada valor en su respectiva columa (en el caso de la columna acciones no sera ocupado por ningun valor).
Modulo `main.py`

```python
        # nuestro registro de datos
        datolista=[
                ['A1','Valeria','valeria@gmail.com','25'],
                ['A2','Jeronima','jeronima@gmail.com','35'],
                ['A3','Santiago','santiago@gmail.com','78'],
                ['A4','Javier','javier@gmail.com','58'],
                ['A5','Thomas','thomas@gmail.com','25'],
                ['A6','Pedro','pedro@gmail.com','42'],
                ]
```
|  ID | Nombre  | Correo  | Edad  | Acciones  |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| A1  |  Valeria | valeria@gmail.com  | 25  |  `Editar` `Eliminar`  |
| A2  |  Jeronima | jeronima@gmail.com  | 35  |  `Editar` `Eliminar`  |
# Diseño
Para cambiar la apariencia de los botones, solo es necesario pasar los parametros indicados, entre ellos se encuentra la hoja de estilos.
Modulo `accionestabla.py`
```python
            # CREAR BOTONES /*/*/*/*/*/*/*/*/*/*/*/*/*/
            btn_uno = self.creabotones(
                estilo = (u"""
                          QPushButton{background-color: #52CF33; color: white}"
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
```

# Previsualización

![](https://1.bp.blogspot.com/-MI1_8MWh6lQ/YErKo7FeGDI/AAAAAAAAAEs/R12yjqT7WlgKVu68AyHldMH8P0glevYzgCLcBGAsYHQ/s1600/1A.jpg)