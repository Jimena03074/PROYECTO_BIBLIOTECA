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

class LibroWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Agregar_Libro.ui", self)
        self.setWindowTitle("Agregar Libro")
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Actualizar_Libro.ui", self)
        self.setWindowTitle("Modificar Libro")
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Eliminar_Libro.ui", self)
        self.setWindowTitle("Eliminar Libro")
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Consultar_Libro.ui", self)
        self.setWindowTitle("Consultar Libro")
        uic.loadUi("D:/PROYECTO_FINAl_BIBLIOTECA/Ventanas/Libro_menu.ui", self)
        self.setWindowTitle("Agregar Libro")
        
        
       
       
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","biblioteca")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
       
        #BOTONES DE MENU
        self.pbAgregar_Li.clicked.connect(self.BotonAgregar_Libro_clicked)
        self.pbActualizar_Li.clicked.connect(self.BotonModificar_Libro_clicked)
        self.pbConsultar_Li.clicked.connect(self.BotonConsultar_Libro_clicked)
        self.pbEliminar_Li.clicked.connect(self.BotonEliminar_Libro_clicked)
        self.pbMenuG.clicked.connect(self.volverG)
        
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_Libro.clicked.connect(self.AgregarLibro_clicked)
        self.pbLimpiar_Libro.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_Libro.clicked.connect(self.BotonVolverMenu_Li_clicked)
        
       
    
    
    
    
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
    
    
    
    
    #--------AGREGAR Libro-------------------------------------------------------------------
    #declaracion de la funcion para el boton guardar        
    def AgregarLibro_clicked(self):
        try:
            #ASIGNAR VALORES DE ENTRADA PARA CONSULTAR
            codigo = str(self.lineEdit_CodigoL.text())
            cod = len(codigo) #curp1
            
            consulta = '''SELECT codigo from libros WHERE codigo=%s'''  
            self.cursor.execute(consulta,codigo)
            row = self.cursor.fetchone()
            
            
            if cod==10  and row == None: #Corrobora que no exista el datos a ingresar
                
                titulo = str(self.lineEdit_Titulo.text())
                autor=str(self.lineEdit_Autor.text())
                edicion=str(self.lineEdit_Edicion.text())
                editorial=str(self.lineEdit_Editorial.text())
                año=str(self.lineEdit_Anio.text())
                acervo=str(self.lineEdit_Acervo.text())
                inserta_registros = '''insert into libros(codigo, titulo, autor, edicion, editorial, año,acervo)
                values(%s,%s,%s,%s,%s,%s,%s)'''
                datos=(codigo,titulo, autor, edicion, editorial, año,acervo)
                self.cursor.execute(inserta_registros,datos)
                self.con.commit()
                
            else:
                raise ValueError
            
        except ValueError :
            QMessageBox.information(self,"NO GUARDADO","VERIFICA EL CODIGO DEL LIBRO",QMessageBox.Ok)#falta arreglar
                
        else:
            #Limpia por completo el formulario
            self.lineEdit_CodigoL.setText('')
            self.lineEdit_Titulo.setText('')
            self.lineEdit_Autor.setText('')
            self.lineEdit_Edicion.setText('')
            self.lineEdit_Editorial.setText('')
            self.lineEdit_Anio.setText('')
            self.lineEdit_Acervo.setText('')
            
            QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
        finally:
            print(" TERMINADO")
        
    #----------------ELIMINAR PACIENTE-----------------------------------------------------------
    #funcion para eliminar datos    
    def EliminarLibro_clicked(self):
        try:
            codigo = str(self.lineEdit_CodigoL.text())
            consulta  ='''SELECT * from libros WHERE codigo=%s''' #% ELI
            self.cursor.execute(consulta,codigo)
            row = self.cursor.fetchone()
            
            if row != None:
                reply = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER ELIMINAR ESTE LIBRO?",
                        QMessageBox.Yes, QMessageBox.No)
                
                if reply == QMessageBox.Yes:
                    eliminar_registro = '''DELETE FROM libros WHERE codigo=%s'''
                    self.cursor.execute(eliminar_registro,codigo)
                    self.con.commit()
                    QMessageBox.information(self, "EXITOSO","LIBRO ELIMINADO", QMessageBox.Ok)
                else:
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
            QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","EL LIBRO NO EXISTE",QMessageBox.Ok)
        else:
            self.lineEdit_CodigoL.setText('')
            self.lineEdit_Titulo.setText('')
            self.lineEdit_Autor.setText('')
            self.lineEdit_Edicion.setText('')
            self.lineEdit_Editorial.setText('')
            self.lineEdit_Anio.setText('')
            self.lineEdit_Acervo.setText('')
        finally:
            print(" TERMINADO")
    
    
    
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #FUNCION MODIFICAR*********************************************************************************
    def Modificar_clicked(self):
        try:
            titulo = str(self.lineEdit_Titulo.text())
            autor=str(self.lineEdit_Autor.text())
            edicion=str(self.lineEdit_Edicion.text())
            editorial=str(self.lineEdit_Editorial.text())
            año=str(self.lineEdit_Anio.text())
            acervo=str(self.lineEdit_Acervo.text())
            
            codigo = str(self.lineEdit_CodigoL.text())
            consultar_registro = '''SELECT * from libros WHERE codigo=%s'''
            self.cursor.execute(consultar_registro,codigo)
            row = self.cursor.fetchone()
            
            if  row != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTE LIBRO?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE libros SET titulo= %s, autor= %s, edicion= %s, editorial= %s, año= %s,acervo=%s WHERE codigo= %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(titulo, autor,edicion,editorial,año,acervo,codigo))
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSOSO","DATOS ACTUALIZADOS",QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
               QMessageBox.information(self,"NO ACTUALIZADO","CANCELADO",QMessageBox.Ok)
        
        except ArithmeticError :
               QMessageBox.information(self,"ERROR","EL Libro NO EXISTE, VERIFICA EL CODIGO",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            #self.lineEdit_CodigoL.setText('')
            self.lineEdit_Titulo.setText('')
            self.lineEdit_Autor.setText('')
            self.lineEdit_Edicion.setText('')
            self.lineEdit_Editorial.setText('')
            self.lineEdit_Anio.setText('')
            self.lineEdit_Acervo.setText('')
        finally:
            print(" TERMINADO")
    
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
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ LIBROS?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 


    ##IR A MENU------------------
    def BotonVolverMenu_Li_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAl_BIBLIOTECA/Ventanas/Libro_menu.ui", self)
        self.setWindowTitle("MENU")  
        
        LibroWindowClass()#ACCION AGREGAR
        
        #BOTONES DE MENU
        self.pbAgregar_Li.clicked.connect(self.BotonAgregar_Libro_clicked)
        self.pbActualizar_Li.clicked.connect(self.BotonModificar_Libro_clicked)
        self.pbConsultar_Li.clicked.connect(self.BotonConsultar_Libro_clicked)
        self.pbEliminar_Li.clicked.connect(self.BotonEliminar_Libro_clicked)
        self.pbMenuG.clicked.connect(self.volverG)
        
      
    #>>>IR A AGREGAR
    def BotonAgregar_Libro_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Agregar_Libro.ui", self)
        self.setWindowTitle("Agregar Libro")

        LibroWindowClass()#ACCION AGREGAR 
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_Libro.clicked.connect(self.AgregarLibro_clicked)
        
        self.pbLimpiar_Libro.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_Libro.clicked.connect(self.BotonVolverMenu_Li_clicked)
        
    #>>>IR A ELIMINAR 
    def BotonEliminar_Libro_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Eliminar_Libro.ui", self)
        self.setWindowTitle("Eliminar Libro")
        
        LibroWindowClass()#ACCION AGREGAR 
        self.pbEliminar_Libro.clicked.connect(self.EliminarLibro_clicked)
        self.pbConsultar_Libro.clicked.connect(self.Consultar_clicked)  
        
   
        self.pbLimpiar_Libro.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_Libro.clicked.connect(self.BotonVolverMenu_Li_clicked)
        
         
        
    #>>>IR A CONSULTAR
    def BotonConsultar_Libro_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Consultar_Libro.ui", self)
        self.setWindowTitle("CONSULTAR PACIENTE") 
        
        LibroWindowClass()#ACCION AGREGAR 
        self.pbConsultarL.clicked.connect(self.Consultar_clicked)
        
        self.pbLimpiar_Libro.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_Libro.clicked.connect(self.BotonVolverMenu_Li_clicked)
        
        
    #>>>IR A MODIFICAR
    def BotonModificar_Libro_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Actualizar_Libro.ui", self)
        self.setWindowTitle("ACTUALIZAR Libro") 
        LibroWindowClass()#ACCION AGREGAR 
        
        self.pbModificar_Libro.clicked.connect(self.Modificar_clicked)
        self.pbConsultar_Libro.clicked.connect(self.Consultar_clicked)
        
        self.pbLimpiar_Libro.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_Libro.clicked.connect(self.BotonVolverMenu_Li_clicked)
        
        
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = LibroWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())
        