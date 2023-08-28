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

from ACERVO import AcervoWindowClass
from ALUMNOS import AlumnoWindowClass
from LIBROS import LibroWindowClass
from menuAdministrador import MenuAdministradorWindowClass


class UsuarioWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/login_Alumno.ui", self)
        self.setWindowTitle("Consultar Alumno")
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","biblioteca")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
       
     
        #BOTONES DE AGREGAR--------------------------------------
        self.pbAcceder_alumno.clicked.connect(self.Consultar_clicked)
        
    
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #declaracion de la funcion para el boton consultar    
    def Consultar_clicked(self):
        try:
            usuario = str(self.lineEdit_Usuario.text())
            log = str(self.lineEdit_login.text())
            
            consultar_registro = '''SELECT * from usuarios WHERE nombre=%s'''
            self.cursor.execute(consultar_registro,usuario)
            row = self.cursor.fetchone()
            
            consultar_registro2 = '''SELECT * from usuarios WHERE contraseña=%s'''
            self.cursor.execute(consultar_registro2,log)
            row2 = self.cursor.fetchone()
                
            if  row != None and row2 != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_Usuario.setText('')
                self.lineEdit_loguin.setText('')
            
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA LA MATRICULA",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            print('entro')
            
        finally:
            print(" TERMINADO")
    
    
    def Abrir(self):
        self.menu = MenuAdministradorWindowClass()
    
    
    
    def AbrirMenu(self):
        self.menu.show()

        
        
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = UsuarioWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())
        