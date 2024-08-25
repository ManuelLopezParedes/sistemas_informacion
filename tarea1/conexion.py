# necesitamos importar la libreria usando *pip install mysql-connector* en nuestra terminal
import mysql.connector

info= input("escribe tu nombre ",)

conexion=mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="",
                                database="base")
cursor=conexion.cursor()
sql="insert into nombre (datos) value (%s)"
datos = (info,)
cursor.execute(sql, datos)

conexion.commit()

with open('datos.txt', 'a') as archivo:
    archivo.write(info + " se guardo en la base de datos \n" )


conexion.close()