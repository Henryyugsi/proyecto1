import pymysql
class DataBase:
    def __init__(self):
        self.connection= pymysql.connect(host="localhost",user="root",password="",db="iot")
        self.cursor=self.connection.cursor()

    def select_user(self,id):
        sql='SELECT ID, NOMBRE, FECHA, VALOR FROM sensores WHERE ID ={}'.format(id)
        try:
            self.cursor.execute(sql)
            user=self.cursor.fetchone()
            print("ID: ", user[0])
            print("NOmbre: ", user[1])
            print("FECHA: ", user[2])
            print("VALOR: ", user[3])
        except Exception as e:
            raise

    def insertDatos(self,nombre,fecha,valor):
        sql="INSERT INTO sensores(NOMBRE,FECHA,VALOR) VALUES('{}','{}',{})".format(nombre,fecha,valor)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se ha insertado correctamente")
        except Exception as e:
            raise

    def cerrar(self):
        self.connection.close()
        print("Se ha finalizado correctamente")

database=DataBase()
database.select_user(14)
database.insertDatos('Humedad','2022-11-04',23)
database.cerrar()
##Instalar Libreria
#pip install PyMySQL






