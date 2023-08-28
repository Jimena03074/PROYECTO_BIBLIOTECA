#Autor: Jimena Leon Garcia
#Matricula: 181803074
#Fecha de creacion: 26/03/2023
#Proyecto: Sistema de biblioteca
#Modulo del sistema: Modulo de Alumnos
#Version: 1.0

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from bd import ConexionBD


class AcervoWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Agregar_Acervo.ui", self)
        self.setWindowTitle("Agregar Acervo")
        
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Actualizar_Acervo.ui", self)
        self.setWindowTitle("Modificar Acervo")
        
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Eliminar_Acervo.ui", self)
        self.setWindowTitle("Eliminar Acervo")
        
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Consultar_Acervo.ui", self)
        self.setWindowTitle("Consultar Acervo")
        
        uic.loadUi("D:/PROYECTO_FINAl_BIBLIOTECA/Ventanas/Acervo_menu.ui", self)
        self.setWindowTitle("Acervo")
        
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","biblioteca")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
        #BOTONES DE MENU------
        
        self.pbAgregar_ace.clicked.connect(self.BotonAgregar_acervo_clicked)
        self.pbActualizar_ace.clicked.connect(self.BotonModificar_acervo_clicked)
        self.pbConsultar_ace.clicked.connect(self.BotonConsultar_acervo_clicked)
        self.pbEliminar_ace.clicked.connect(self.BotonEliminar_acervo_clicked)
        self.pbMenuA.clicked.connect(self.volverG)
        
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_Acervo.clicked.connect(self.AgregarAcervo_clicked)
        
        self.pbLimpiar_Acervo.clicked.connect(self.BotonLimpiar_clicked)
        self.pbRegresar_Acervo.clicked.connect(self.BotonVolverMenu_clicked)
    
        
    
    
    #Boton para limpieza del formulario
    def BotonLimpiar_clicked(self):
        self.lineEdit_codigoA.setText('')
        self.lineEdit_nombreAcervo.setText('')
        self.lineEdit_DescripcionAcervo.setText('')
        self.con.commit()
    
    
    
    #--------AGREGAR TUTOR---------
    #declaracion de la funcion para el boton guardar    
    def AgregarAcervo_clicked(self):
        try:
            #ASIGNAR VALORES DE ENTRADA
            codigoA = str(self.lineEdit_codigoA.text())
            cod = len(codigoA)
            consulta = '''SELECT codigoA from acervo WHERE codigoA=%s'''  
            self.cursor.execute(consulta,codigoA)
            row = self.cursor.fetchone() 
            
            if row == None and cod == 6: #Corrobora que no exista el datos a ingresar
                #se declaran variables para las entradas de datos
                nombre=str(self.lineEdit_nombreAcervo.text())
                desc=str(self.lineEdit_DescripcionAcervo.text())
               
                
                inserta_registros = '''insert into acervo(codigoA, nombre, descripcion)
                values(%s,%s,%s)'''
                datos = (codigoA, nombre, desc)
                self.cursor.execute(inserta_registros,datos)
                
            else:
                raise ValueError
        except ValueError:
            QMessageBox.information(self,"NO GUARDADO","VERIFICA LOS DATOS",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #Limpia por completo el formulario
            self.lineEdit_codigoA.setText('')
            self.lineEdit_nombreAcervo.setText('')
            self.lineEdit_DescripcionAcervo.setText('')
            
            self.con.commit()
            QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
            
        finally:
            print(" TERMINADO")
    
    
    
    #--------------ELIMINAR TUTOR---------------------------------------------
    def EliminarAcervo_clicked(self):
        try:
            codigoA = str(self.lineEdit_codigoA.text())
            consulta = '''SELECT codigoA from acervo WHERE codigoA=%s''' 
            self.cursor.execute(consulta,codigoA)
            row = self.cursor.fetchone() 
            
            if row != None:
                reply = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER ELIMINAR ESTE ACERVO?",
                                               QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    eliminar_registro  ='''DELETE from acervo WHERE codigoA=%s''' #% ELI
                    row=self.cursor.execute(eliminar_registro,codigoA)
                    self.con.commit()
                    QMessageBox.information(self, "EXITOSO","ACERVO ELIMINADO", QMessageBox.Ok)
                else:
                    raise ValueError
            else:
                raise ArithmeticError
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","CANCELADO",QMessageBox.Ok)
        except ValueError :
            QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
            
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEdit_nombreAcervo.setText('')
            self.lineEdit_DescripcionAcervo.setText('')
        finally:
            print(" TERMINADO")
    
    
     #FUNCION CONSULTAR*********************************************************************************
    def ConsultarAcervo_clicked(self):
        try:
            codigoA = str(self.lineEdit_codigoA.text())
            consulta = '''SELECT * from acervo WHERE codigoA=%s''' 
            self.cursor.execute(consulta,codigoA)
            row = self.cursor.fetchone() 
            
            if row != None:
               print('')
            else:
                self.lineEdit_nombreAcervo.setText('')
                self.lineEdit_DescripcionAcervo.setText('')
                
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL ACERVO NO EXISTE, VERIFICA EL CODIGO",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_nombreAcervo.setText(str(row[1]))
            self.lineEdit_DescripcionAcervo.setText(str(row[2]))
          
        finally:
            print(" TERMINADO")
   
    
    
     #FUNCION MODIFICAR*********************************************************************************
    def ModificarAcervo_clicked(self):
        try:
            nombre=int(self.lineEdit_nombreAcervo.text())
            desc=str(self.lineEdit_DescripcionAcervo.text())
                
                
            codigoA = str(self.lineEdit_codigoA.text())
            consultar_registro = '''SELECT * from acervo WHERE codigoA=%s'''
            self.cursor.execute(consultar_registro,codigoA)
            row = self.cursor.fetchone()
            print('todo bien')
            
            if  row != None:
                print('todo bien')
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTE ACERVO?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE acervo SET nombre= %s, descripcion= %s WHERE codigoA = %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(nombre,desc,codigoA))
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSOSO","DATOS ACTUALIZADOS",QMessageBox.Ok)
                else: 
                    print('no entra')
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
            QMessageBox.information(self,"NO ACTUALIZADO","CANCELADO",QMessageBox.Ok)
        
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","EL ACERVO NO EXISTE, VERIFICA El CODIGO",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEdit_nombreAcervo.setText('')
            self.lineEdit_DescripcionAcervo.setText('')
        finally:
            print(" TERMINADO")
            

        
    def volverG(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ ACERVO?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 
     
        
    ##IR A MENU------------------
    def BotonVolverMenu_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAl_BIBLIOTECA/Ventanas/Acervo_menu.ui", self)
        self.setWindowTitle("Acervo") 
        
        AcervoWindowClass()#ACCION AGREGAR
        
        #BOTONES DE MENU
        #BOTONES DE MENU------
        
        self.pbAgregar_ace.clicked.connect(self.BotonAgregar_acervo_clicked)
        self.pbActualizar_ace.clicked.connect(self.BotonModificar_acervo_clicked)
        self.pbConsultar_ace.clicked.connect(self.BotonConsultar_acervo_clicked)
        self.pbEliminar_ace.clicked.connect(self.BotonEliminar_acervo_clicked)
        self.pbMenuA.clicked.connect(self.volverG)
        
    #>>>IR A AGREGAR
    def BotonAgregar_acervo_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Agregar_Acervo.ui", self)
        self.setWindowTitle("Agregar Acervo")

        AcervoWindowClass()#ACCION AGREGAR 
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_Acervo.clicked.connect(self.AgregarAcervo_clicked)
        
        self.pbLimpiar_Acervo.clicked.connect(self.BotonLimpiar_clicked)
        self.pbRegresar_Acervo.clicked.connect(self.BotonVolverMenu_clicked)
    
    #>>>IR A ELIMINAR 
    def BotonEliminar_acervo_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Eliminar_Acervo.ui", self)
        self.setWindowTitle("Eliminar Acervo")
        
        AcervoWindowClass()#ACCION AGREGAR
        self.pbEliminar_ace.clicked.connect(self.EliminarAcervo_clicked)

        self.pbLimpiar_ace.clicked.connect(self.BotonLimpiar_clicked)
        self.pbConsultar_ace.clicked.connect(self.ConsultarAcervo_clicked)
        self.pbRegresar_ace.clicked.connect(self.BotonVolverMenu_clicked)
        
    
    #>>>IR A CONSULTAR
    def BotonConsultar_acervo_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Consultar_Acervo.ui", self)
        self.setWindowTitle("Consultar Acervo")
        
        AcervoWindowClass()#ACCION AGREGAR
        
        self.pbConsultar_ace.clicked.connect(self.ConsultarAcervo_clicked)
        self.pbLimpiar_ace.clicked.connect(self.BotonLimpiar_clicked)
        self.pbRegresar_ace.clicked.connect(self.BotonVolverMenu_clicked)
        
    
    
    #>>>IR A MODIFICAR
    def BotonModificar_acervo_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Actualizar_Acervo.ui", self)
        self.setWindowTitle("Modificar Acervo")
        AcervoWindowClass()#ACCION AGREGAR
        
        self.pbConsultar_Acervo.clicked.connect(self.ConsultarAcervo_clicked)
        self.pbModificar_Acervo.clicked.connect(self.ModificarAcervo_clicked)
                
        self.pbLimpiar_Acervo.clicked.connect(self.BotonLimpiar_clicked)
        self.pbRegresar_Acervo.clicked.connect(self.BotonVolverMenu_clicked)
        
       
    
    
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = AcervoWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())