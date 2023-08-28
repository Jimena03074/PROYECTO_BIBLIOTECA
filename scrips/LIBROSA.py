#Autor: Jimena Leon Garcia
#Matricula: 181803074
#Fecha de creacion: 26/03/2023
#Proyecto: Sistema de biblioteca
#Modulo del sistema: Modulo de Libros
#Version: 1.0

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from bd import ConexionBD

class LibroAWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Consultar_Libro.ui", self)
        self.setWindowTitle("CONSULTAR LIBRO") 
       
       
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","biblioteca")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
       
        #BOTONES DE MENU
        self.pbConsultarL.clicked.connect(self.Consultar_clicked)
        self.pbLimpiar_Libro.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_Libro.clicked.connect(self.volverG)
        
        
       
       
    
    
    
    
    #Boton para limpieza del formulario
    def BotonCancelar_clicked(self):
        #Limpia por completo el formulario
        self.lineEdit_CodigoL.setText('')
        self.lineEdit_Titulo.setText('')
        self.lineEdit_Autor.setText('')
        self.lineEdit_Edicion.setText('')
        self.lineEdit_Editorial.setText('')
        self.lineEdit_Anio.setText('')
        self.lineEdit_Acervo.setText('')
            
        self.con.commit()
    
    
    
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #declaracion de la funcion para el boton consultar    
    def Consultar_clicked(self):
        try:
            codigo = str(self.lineEdit_CodigoL.text())
            cod = len(codigo) #curp1
            consultar_registro = '''SELECT * from libros WHERE codigo=%s'''
            self.cursor.execute(consultar_registro,codigo)
            row = self.cursor.fetchone()
                
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_Titulo.setText('')
                self.lineEdit_Autor.setText('')
                self.lineEdit_Edicion.setText('')
                self.lineEdit_Editorial.setText('')
                self.lineEdit_Anio.setText('')
                self.lineEdit_Acervo.setText('')
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","EL LIBRO NO EXISTE, VERIFICA EL CODIGO",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_Titulo.setText(str(row[1]))
            self.lineEdit_Autor.setText(str(row[2]))
            self.lineEdit_Edicion.setText(str(row[3]))
            self.lineEdit_Editorial.setText(str(row[4]))
            self.lineEdit_Anio.setText(str(row[5]))
            self.lineEdit_Acervo.setText(str(row[6]))

        finally:
            print(" TERMINADO")
            
            
   

    #--------------------------------------------------BIENE---------------------------------------------------------------------------------
        
    def volverG(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE LIBROS?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 

     
        
        
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = LibroAWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())
        