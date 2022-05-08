import socket
import csv
import uuid

def writetocsv(data):
	# data = ['toyota','red','1A11','1001','2022-05-07 15:29:15']
	with open('2-car-system-in.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data) # no s is single line append
	print('csv saved')
############ADRESS##############
serverip = '192.168.0.100'
port = 9000
buffsize = 4096

car_dict = {}

while True:
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.bind((serverip,port))
	server.listen(1)
	print('waiting client...')

	client, addr = server.accept()
	print('connected from:', addr)

	data = client.recv(buffsize).decode('utf-8')
	print('Data from client: ',data)

	source = data.split('|')[0] # มาจากโปรแกรมฝั่งไหน? in / location / check

	if source == 'in':
		key = str(uuid.uuid1()).split('-')[0]
		car_dict[key] = data.split('|')
		# - บันทึกข้อมูลที่ได้รับจาก [2]
		# write to csv
		writetocsv(data.split('|'))
		client.send('saved'.encode('utf-8'))
		client.close()
	elif source == 'location':
		text = 'out|'
		for k,v in car_dict.items():
			text += k + '|'
			for dt in v:
				text += dt + '|'

		print('Send to Location: ', text)
		client.send(text.encode('utf-8'))
		client.close()
	else:
		pass


	

	


















'''
[1]-car-system-out.py
	- server.py
	(function)
		- บันทึกเวลาออก
		- คำนวณชั่วโมงจอด
		- คำนวณค่าจอด
		- บันทึกข้อมูลที่ได้รับจาก [2]
'''