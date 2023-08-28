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

class RenovarWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Renovar_Prestamo.ui", self)
        self.setWindowTitle("Renovar prestamo")

       
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","biblioteca")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
       
      
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar.clicked.connect(self.Agregarclicked)
        self.pbLimpiar.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar.clicked.connect(self.volverG)
        
       
    
    
    #Boton para limpieza del formulario
    def BotonCancelar_clicked(self):
        #Limpia por completo el formulario
        self.lineEdit_Matricula.setText('')
        self.llineEdit_CodigoLibro.setText('')
        self.lineEdit_Fecha.setText('')
        self.lineEdit_NuevaFecha.setText('')
        self.con.commit()
    
    
    #--------AGREGAR Libro-------------------------------------------------------------------
    #declaracion de la funcion para el boton guardar        
    def Agregarclicked(self):
        try:
            #ASIGNAR VALORES DE ENTRADA PARA CONSULTAR
            mat = str(self.lineEdit_Matricula.text())
            ace = str(self.lineEdit_CodigoAcervo.text())
            lib = str(self.lineEdit_CodigoLibro.text())
            
            
            consulta = '''SELECT codigo from libros WHERE codigo=%s'''  
            self.cursor.execute(consulta,lib)
            row = self.cursor.fetchone()
            
            consulta2 = '''SELECT codigoA from acervo WHERE codigoA=%s'''  
            self.cursor.execute(consulta2,ace)
            row2 = self.cursor.fetchone()
            
            
            if row2!=None  and row !=None: #Corrobora que no exista el datos a ingresar
                
                feI = str(self.lineEdit_fecha1.text())
                feF=str(self.lineEdit_fecha2.text())
                inserta_registros = '''insert into prestamos(matricula, codigoA,codigo, fecha_inicio, fecha_fin)
                values(%s,%s,%s,%s,%s)'''
                datos=(mat,ace, lib, feI, feF)
                self.cursor.execute(inserta_registros,datos)
                self.con.commit()
                
            else:
                raise ValueError
            
        except ValueError :
            QMessageBox.information(self,"NO GUARDADO","VERIFICA EL CODIGO DEL LIBRO",QMessageBox.Ok)#falta arreglar
                
        else:
            #Limpia por completo el formulario
            self.lineEdit_Matricula.setText('')
            self.lineEdit_CodigoAcervo.setText('')
            self.lineEdit_CodigoLibro.setText('')
            self.lineEdit_fecha1.setText('')
            self.lineEdit_fecha2.setText('')
            
            QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
        finally:
            print(" TERMINADO")
        
        
        
    #--------------------------------------------------BIENE---------------------------------------------------------------------------------
        
    def volverG(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE PRESTAMOS?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 

        
        
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = RenovarWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())
        