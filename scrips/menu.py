
from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
import pandas as pd
from bd import ConexionBD
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from ACERVO import AcervoWindowClass
from ALUMNOS import AlumnoWindowClass
from LIBROS import LibroWindowClass
from PRESTAMOS import PrestamoWindowClass
from LIBROSA import LibroAWindowClass
from RENOVAR import RenovarWindowClass


class MenuWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/login_Alumno.ui", self)
        self.setWindowTitle("Consultar Alumno")
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","biblioteca")
        self.cursor = self.con.cursor()
        
      
        #BOTONES --------------------------------------
        self.pbAcceder_alumno.clicked.connect(self.Consulta)
        
        
        
        #-----------ADMNISTRADOR------------
        #objeto de alumno instanciado
        self.alumno = AlumnoWindowClass()
        
        #objeto de tutor instanciado
        self.acervo = AcervoWindowClass()
        
        #objeto de acervo instanciado
        self.libro = LibroWindowClass()
        
        
        #objeto de acervo instanciado
        self.prestamo = PrestamoWindowClass()
        
        
        #-----------ALUMNOS------------
        
        #objeto de alumno instanciado
        self.libroA = LibroAWindowClass()
        
        #objeto de acervo instanciado
        self.renovar = RenovarWindowClass()
        
          #Funcion que me permite abrir los .py de administrador
    def AbrirAlumno(self):
        self.alumno.show()
    
    def AbrirAcervo(self):
        self.acervo.show()
        
    def AbrirLibro(self):
        self.libro.show()
    
    def AbrirPrestamo(self):
        self.prestamo.show()
        
    #Funcion que me permite abrir los py de alumnos
    def AbrirLibroA(self):
        self.libroA.show()
    
    def AbrirRenovar(self):
        self.renovarshow()
        
        
    def Consulta(self):
        try:
            usuario = str(self.lineEdit_Usuario.text())
            log = str(self.lineEdit_login.text())
            
            
            #---------------
            consultar_registro = '''SELECT * from administradores WHERE nombre=%s'''
            self.cursor.execute(consultar_registro,usuario)
            row = self.cursor.fetchone()
            
            consultar_registro2 = '''SELECT * from administradores WHERE contraseña=%s'''
            self.cursor.execute(consultar_registro2,log)
            row2 = self.cursor.fetchone()
            
            
            if  row != None and row2 != None:
                print(" ")
                uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/MENU_ADMINISTRADOR.ui", self)
                self.setWindowTitle("MENU ADMINISTRADOR") 
                MenuWindowClass()
                
                
                #BOTONES DE MENU GENERAL 
                self.pbAlumnos.clicked.connect(self.AbrirAlumno) #ACCION IR A VAC
                self.pbAcervos.clicked.connect(self.AbrirAcervo) #ACCION IR A VAC
                self.pbLibros.clicked.connect(self.AbrirLibro) #ACCION IR A VAC
                self.pbPrestamos.clicked.connect(self.AbrirPrestamo) #ACCION IR A VAC  
                self.pbSalir.clicked.connect(self.salir) #ACCION IR A VAC
                
                
            else:
                consultar_registro = '''SELECT * from usuarios WHERE nombre=%s'''
                self.cursor.execute(consultar_registro,usuario)
                row3 = self.cursor.fetchone()
                
                consultar_registro2 = '''SELECT * from usuarios WHERE contraseña=%s'''
                self.cursor.execute(consultar_registro2,log)
                row4 = self.cursor.fetchone()
                
                if row3 != None and row4 != None:
                    print("")
                    uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/MENU_ALUMNO.ui", self)
                    self.setWindowTitle("MENU ALUMNO")  
                
                    #BOTONES DE MENU GENERAL 
                    self.pbLibros.clicked.connect(self.AbrirLibroA) #ACCION IR A VAC
                    self.pbRePrestamos.clicked.connect(self.AbrirRenovar) #ACCION IR A VAC
                    self.pbSalir.clicked.connect(self.salir) #ACCION IR A VAC
                else:
                    raise ValueError

        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","EL USUARIO NO EXISTE, VERIFICA LOS DATOS",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            print('entro')
        finally:
            print(" TERMINADO")
 
    
    def administrador(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/MENU_ADMINISTRADOR.ui", self)
        self.setWindowTitle("MENU ADMINISTRADOR")  
        
        #BOTONES DE MENU GENERAL 
        self.pbAlumnos.clicked.connect(self.AbrirAlumno) #ACCION IR A VAC
        self.pbAcervos.clicked.connect(self.AbrirAcervo) #ACCION IR A VAC
        self.pbLibros.clicked.connect(self.AbrirLibro) #ACCION IR A VAC
        self.pbPrestamos.clicked.connect(self.AbrirPrestamo) #ACCION IR A VAC
        self.pbSalir.clicked.connect(self.salir) #ACCION IR A VAC
       
    
    
    def alumnos(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/MENU_ALUMNO.ui", self)
        self.setWindowTitle("MENU ALUMNO")  
       
        #BOTONES DE MENU GENERAL 
        self.pbLibros.clicked.connect(self.AbrirLibroA) #ACCION IR A VAC
        self.pbRePrestamos.clicked.connect(self.AbrirRenovar) #ACCION IR A VAC
        self.pbSalir.clicked.connect(self.salir) #ACCION IR A VAC
    
    def salir(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show()
        
        


    
if __name__ == '__main__':
    app = QApplication([])
    main = MenuWindowClass()
    main.show()
    sys.exit(app.exec())
    
    
    
        
        
