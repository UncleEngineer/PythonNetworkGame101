#guiclient.py
import socket
server_ip = '192.168.1.163'
port = 7000


for i in range(5):
	data = input('Send: ')
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((server_ip,port))
	server.send(data.encode('utf-8'))

	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ',data_server)
	server.close()

#########DEF##########

def SendMessage(data):
	#data = input('Send: ')
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((server_ip,port))
	server.send(data.encode('utf-8'))

	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ',data_server)
	server.close()