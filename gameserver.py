import socket
server_ip = '192.168.1.150'
port = 8000
# -*- coding: utf-8 -*-

allplayer = {}

def Server():
	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		server.bind((server_ip,port))
		server.listen(1)
		print('Waiting for client')

		client, addr = server.accept() #ถ้ามีการติดต่อเข้ามาให้สร้างตัวเชื่อมต่อ
		print('Connected from: ', [str(addr)])
		data = client.recv(1024).decode('utf-8')
		print('Message: ', data)
		client_ip = str(addr).split("'")[1]
		data_cmd = data.split('|')
		allplayer[client_ip] = {'name':data_cmd[2],'ip':client_ip}
		print(allplayer)

Server()