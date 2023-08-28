import pymysql
class ConexionBD():
    #CREACR LA CONECION
    def CreateDBConnection(self, servidor, port, user, password, database):
        connection = pymysql.connect(host = servidor, 
                                     port = port,  
                                     user = user,  
                                     password =password, 
                                     db = database)
        return connection 

    #cerrar la conexion
    def closeDBConnection(self,connection):
        try:
            connection.close()
            print("CONEXION CERRADA")
        except pymysql.ProgrammingError as e:
            print(e)

if __name__=="__main__":
    prueba = ConexionBD()
    con = prueba.CreateDBConnection("localhost",3306,"root","","biblioteca")
    cursor = con.cursor()

    """#COLSULTAR EN LA BD--
    cursor.execute("SELECT * from coche")
    row = cursor.fetchone()

    print (row)
    while row:
        print("ID=%d Modelo=%s Color=%s  Modelo=%s" %(row[0], row[1], row[2], row[3]))
        row = cursor.fetchone()"""