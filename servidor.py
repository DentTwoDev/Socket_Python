import socket
import sys

# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 # Puerto de comunicacion
sock.bind(('localhost',port)) # IP y Puerto de conexion en una Tupla

print ("esperando conexiones en el puerto ", port)
# Vamos a esperar que un cliente se conecte
# Mientras tanto el script se va a pausar
sock.listen(5)
# Cuando un cliente se conecte vamos a obtener la client_addr osea la direccion
# tambien vamos a obtener la con, osea la conexion que servira para enviar datos y recibir datos
con, client_addr =  sock.accept()
print "Nueva Conexion establecida con %s:%d" % (client_addr[0] , client_addr[1])

text = "Hola, soy el servidor!" # El texto que enviaremos
con.send(text.encode()) # Enviamos el texto al cliente que se conecta

data = con.recv(4096)
recibido = data.decode()

print(recibido)

if len(recibido) > 1:
	if recibido.rstrip() == "salir":

		recibido = "Cliente desconectado"
		print(recibido)
		con.close()
		sock.close()	
	else:
		
		print(recibido)



#	con.close() # Cerramos la conexion
#	sock.close() # Cerramos el socket

