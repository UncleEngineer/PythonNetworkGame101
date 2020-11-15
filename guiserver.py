#guiserver.py
import socket

def SendMessage(data,server_ip,port):
	#data = input('Send: ')
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((server_ip,port))
	server.send(data.encode('utf-8'))

	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ',data_server)
	server.close()

server_ip = '192.168.1.150'
port = 7500

alluser = [['192.168.1.163',8000],['192.168.1.189',8000],['192.168.1.150',8000]]

global allmessage

allmessage = []


while True:
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.bind((server_ip,port))
	server.listen(1)
	print('Waiting for client')

	client, addr = server.accept() #ถ้ามีการติดต่อเข้ามาให้สร้างตัวเชื่อมต่อ
	print('Connected from: ', addr)
	data = client.recv(1024).decode('utf-8')
	print('Message: ', data)
	allmessage.append(data)

	alltext = 'ALL|'
	for ms in allmessage:
		alltext += ms + '|'

	client.send('We received your message'.encode('utf-8'))
	client.close()

	for us in alluser:
		try:
			SendMessage(alltext, us[0], us[1]) #ส่งข้อความไปหาทุกคนที่อยู่ในลิสต์
		except:
			pass

	

