import socket
from datetime import datetime
############CSV##############
import csv
def writetocsv(data):
	# data = ['toyota','red','1A11','1001','2022-05-07 15:29:15']
	with open('2-car-system-in.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data) # no s is single line append
	print('csv saved')
############ADRESS##############
serverip = '192.168.0.100' # IP of 3-car-system-location.py
port = 9500
buffsize = 4096

while True:

	text = 'check|'
	q = input('Enter Plate No. : ')
	text += q

	# Connect and Send
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(text.encode('utf-8'))
	data_server = server.recv(buffsize).decode('utf-8')
	print('Data from server: ', data_server)
	data_list = data_server.split('|')
	print('Your car zone: ',data_list[-2])
	server.close()
	print('--------------')


'''
[4]-car-system-check.py
	- client-3.py
	(function)
		- ดึงข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร จาก [3]
		- ดึงข้อมูลตำแหน่งโซนของรถจาก [3]
'''