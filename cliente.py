# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 # Puerto de comunicacion
# Realizamos la conexion al la IP y puerto
sock.connect(('localhost',port))
# Leemos los datos del servidor
data = sock.recv(4096)
print(data.decode())
if(len(data) > 0):
	#Definimos el mensaje a enviar en una variable
	mensaje = "El cliente recibio el mensaje"
	sock.send(mensaje.encode())

	entrada = raw_input("> ")
	if entrada.lstrip() == "QUIT":
		mensaje = "salir "
		sock.send(mensaje.encode())
		sock.close()
		sys.exit(0)
	else:
		mensaje = entrada
		sock.send(mensaje.encode())

	#Enviamos el mensaje con send()
	
else:
	# Cerramos el socket
	sock.close()
	# Mostramos los datos recibidos



#--------------Sugerencias---------


'''

entrada = input("> ")
if entrada.rstrip() == "QUIT":
    sock.close()
    sys.exit(0)




sudo lsof -i | grep "py"

sudo kill -9 <process_id>
    '''
