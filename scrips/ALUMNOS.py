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

class AlumnoWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Agregar_Alumno.ui", self)
        self.setWindowTitle("Agregar Alumno")
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Actualizar_Alumno.ui", self)
        self.setWindowTitle("Modificar Alumno")
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Eliminar_Alumno.ui", self)
        self.setWindowTitle("Eliminar Alumno")
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Consultar_Alumno.ui", self)
        self.setWindowTitle("Consultar Alumno")
        uic.loadUi("D:/PROYECTO_FINAl_BIBLIOTECA/Ventanas/Alumno_menu.ui", self)
        self.setWindowTitle("Agregar Alumno")
        
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","biblioteca")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
       
        #BOTONES DE MENU
        self.pbAgregar_alu.clicked.connect(self.BotonAgregar_alumno_clicked)
        self.pbModificar_alu.clicked.connect(self.BotonModificar_alumno_clicked)
        self.pbConsultar_alu.clicked.connect(self.BotonConsultar_alumno_clicked)
        self.pbEliminar_alu.clicked.connect(self.BotonEliminar_alumno_clicked)
        self.pbMenu.clicked.connect(self.volverG)
        
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_alumno.clicked.connect(self.AgregarAlumno_clicked)
        
        self.pbLimpiar_alumno.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_alumno.clicked.connect(self.BotonVolverMenu_alu_clicked)
        
       
    
    
    
    
    #Boton para limpieza del formulario
    def BotonCancelar_clicked(self):
        #Limpia por completo el formulario
        self.lineEdit_matricula.setText('')
        self.lineEdit_contrasena.setText('')
        self.lineEdit_nombre.setText('')
        self.lineEdit_apellidos.setText('')
        self.lineEdit_carrera.setText('')
        self.lineEdit_correo.setText('')
        self.con.commit()
    
    
    
    
    #--------AGREGAR Alumno-------------------------------------------------------------------
    #declaracion de la funcion para el boton guardar        
    def AgregarAlumno_clicked(self):
        try:
            
            #ASIGNAR VALORES DE ENTRADA PARA CONSULTAR
            matricula = str(self.lineEdit_matricula.text())
            mat = len(matricula) #curp1
            
            consulta = '''SELECT matricula from usuarios WHERE  matricula=%s'''  
            self.cursor.execute(consulta,matricula)
            row = self.cursor.fetchone()
            
            
            if mat ==9  and row == None: #Corrobora que no exista el datos a ingresar
                
                contraseña = str(self.lineEdit_contrasena.text())
                nombre=str(self.lineEdit_nombre.text())
                apellidos=str(self.lineEdit_apellidos.text())
                carrera=str(self.lineEdit_carrera.text())
                correo=str(self.lineEdit_correo.text())
                inserta_registros = '''insert into usuarios(matricula, contraseña, nombre, apellidos, carrera, correo)
                values(%s,%s,%s,%s,%s,%s)'''
                datos=(matricula, contraseña, nombre, apellidos, carrera,correo)
                self.cursor.execute(inserta_registros,datos)
                self.con.commit()
                
            else:
                raise ValueError
            
        except ValueError :
            QMessageBox.information(self,"NO GUARDADO","VERIFICA LA MATRICULA DEL ALUMNO",QMessageBox.Ok)#falta arreglar
                
        else:
            #Limpia por completo el formulario
            self.lineEdit_matricula.setText('')
            self.lineEdit_contrasena.setText('')
            self.lineEdit_nombre.setText('')
            self.lineEdit_apellidos.setText('')
            self.lineEdit_carrera.setText('')
            self.lineEdit_correo.setText('')
            QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
        finally:
            print(" TERMINADO")
        
    #----------------ELIMINAR PACIENTE-----------------------------------------------------------
    #funcion para eliminar datos    
    def EliminarAlumno_clicked(self):
        try:
            ELI=str(self.lineEdit_matricula.text())
            consulta  ='''SELECT * from usuarios WHERE matricula=%s''' #% ELI
            self.cursor.execute(consulta,ELI)
            row = self.cursor.fetchone()
            
            if row != None:
                reply = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER ELIMINAR ESTE ALUMNO?",
                        QMessageBox.Yes, QMessageBox.No)
                
                if reply == QMessageBox.Yes:
                    eliminar_registro = '''DELETE FROM usuarios WHERE matricula=%s'''
                    self.cursor.execute(eliminar_registro,ELI)
                    self.con.commit()
                    QMessageBox.information(self, "EXITOSO","ALUMNO ELIMINADO", QMessageBox.Ok)
                else:
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
            QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","EL ALUMNO NO EXISTE",QMessageBox.Ok)
        else:
            self.lineEdit_matricula.setText('')
            self.lineEdit_contrasena.setText('')
            self.lineEdit_nombre.setText('')
            self.lineEdit_apellidos.setText('')
            self.lineEdit_carrera.setText('')
            self.lineEdit_correo.setText('')
        finally:
            print(" TERMINADO")
    
    
    
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #FUNCION MODIFICAR*********************************************************************************
    def Modificar_clicked(self):
        try:
            contraseña = str(self.lineEdit_contrasena.text())
            nombre=str(self.lineEdit_nombre.text())
            apellidos=str(self.lineEdit_apellidos.text())
            carrera=str(self.lineEdit_carrera.text())
            correo=str(self.lineEdit_correo.text())
            
            matricula = str(self.lineEdit_matricula.text())
            mat = len(matricula) #curp1
            consultar_registro = '''SELECT * from usuarios WHERE matricula=%s'''
            self.cursor.execute(consultar_registro,matricula)
            row = self.cursor.fetchone()
            
            if  row != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTE ALUMNO?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE usuarios SET contraseña= %s, nombre= %s, apellidos= %s, carrera= %s, correo= %s WHERE matricula = %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(contraseña, nombre, apellidos, carrera,correo,matricula))
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
               QMessageBox.information(self,"ERROR","EL ALUMNO NO EXISTE, VERIFICA LA MATRICULA",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEdit_contrasena.setText('')
            self.lineEdit_nombre.setText('')
            self.lineEdit_apellidos.setText('')
            self.lineEdit_carrera.setText('')
            self.lineEdit_correo.setText('')
        finally:
            print(" TERMINADO")
    
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #declaracion de la funcion para el boton consultar    
    def Consultar_clicked(self):
        try:
            matricula = str(self.lineEdit_matricula.text())
          
            consultar_registro = '''SELECT * from usuarios WHERE matricula=%s'''
            self.cursor.execute(consultar_registro,matricula)
            row = self.cursor.fetchone()
                
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_contrasena.setText('')
                self.lineEdit_nombre.setText('')
                self.lineEdit_apellidos.setText('')
                self.lineEdit_carrera.setText('')
                self.lineEdit_correo.setText('')
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA LA MATRICULA",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_contrasena.setText(str(row[1]))
            self.lineEdit_nombre.setText(str(row[2]))
            self.lineEdit_apellidos.setText(str(row[3]))
            self.lineEdit_carrera.setText(str(row[4]))
            self.lineEdit_correo.setText(str(row[5]))
        finally:
            print(" TERMINADO")
            
            
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #declaracion de la funcion para el boton consultar    (PARA EL BOTON ELIMINAR)
    def Consultar2_clicked(self):
        try:
            matricula = str(self.lineEdit_matricula.text())
            mat = len(matricula) #curp1
            consultar_registro = '''SELECT * from usuarios WHERE matricula=%s'''
            self.cursor.execute(consultar_registro,matricula)
            row = self.cursor.fetchone()
                
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_contrasena.setText('')
                self.lineEdit_nombre.setText('')
                self.lineEdit_apellidos.setText('')
                self.lineEdit_carrera.setText('')
                self.lineEdit_correo.setText('')
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA LA MATRICULA",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_contrasena.setText(str(row[1]))
            self.lineEdit_nombre.setText(str(row[2]))
            self.lineEdit_apellidos.setText(str(row[3]))
            self.lineEdit_carrera.setText(str(row[4]))
            self.lineEdit_correo.setText(str(row[5]))
        finally:
            print(" TERMINADO")
    

    #--------------------------------------------------BIENE---------------------------------------------------------------------------------

        
    def volverG(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ ALUMNOS?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 


    ##IR A MENU------------------
    def BotonVolverMenu_alu_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAl_BIBLIOTECA/Ventanas/Alumno_menu.ui", self)
        self.setWindowTitle("MENU")  
        
        #ACCION AGREGAR
        
        #BOTONES DE MENU
        self.pbAgregar_alu.clicked.connect(self.BotonAgregar_alumno_clicked)
        self.pbModificar_alu.clicked.connect(self.BotonModificar_alumno_clicked)
        self.pbConsultar_alu.clicked.connect(self.BotonConsultar_alumno_clicked)
        self.pbEliminar_alu.clicked.connect(self.BotonEliminar_alumno_clicked)
        self.pbMenu.clicked.connect(self.volverG)
        
      
    #>>>IR A AGREGAR
    def BotonAgregar_alumno_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Agregar_Alumno.ui", self)
        self.setWindowTitle("Agregar Alumno")

        AlumnoWindowClass()#ACCION AGREGAR 
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_alumno.clicked.connect(self.AgregarAlumno_clicked)
        
        self.pbLimpiar_alumno.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_alumno.clicked.connect(self.BotonVolverMenu_alu_clicked)
        
    #>>>IR A ELIMINAR 
    def BotonEliminar_alumno_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Eliminar_Alumno.ui", self)
        self.setWindowTitle("Eliminar Alumno")
        
        AlumnoWindowClass()#ACCION AGREGAR 
        self.pbEliminar_alumno.clicked.connect(self.EliminarAlumno_clicked)
        self.pbConsultar_alumno.clicked.connect(self.Consultar2_clicked)  
        
   
        self.pbLimpiar_alumno.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_alumno.clicked.connect(self.BotonVolverMenu_alu_clicked)
        
         
        
    #>>>IR A CONSULTAR
    def BotonConsultar_alumno_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Consultar_Alumno.ui", self)
        self.setWindowTitle("CONSULTAR PACIENTE") 
        
        AlumnoWindowClass()#ACCION AGREGAR 
        self.pbConsultarA.clicked.connect(self.Consultar_clicked)
        
        self.pbLimpiar_alumno.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_alumno.clicked.connect(self.BotonVolverMenu_alu_clicked)
        
        
    #>>>IR A MODIFICAR
    def BotonModificar_alumno_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL_BIBLIOTECA/Ventanas/Actualizar_Alumno.ui", self)
        self.setWindowTitle("ACTUALIZAR ALUMNO") 
        AlumnoWindowClass()#ACCION AGREGAR 
        
        self.pbModificar_alumno.clicked.connect(self.Modificar_clicked)
        self.pbConsultar_alumno.clicked.connect(self.Consultar_clicked)
        
        self.pbLimpiar_alumno.clicked.connect(self.BotonCancelar_clicked)
        self.pbRegresar_alumno.clicked.connect(self.BotonVolverMenu_alu_clicked)
        
        
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = AlumnoWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())
        