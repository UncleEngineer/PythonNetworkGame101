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
serverip = '192.168.0.100' # IP of 1-car-system-out.py
port = 9000
buffsize = 4096

while True:
	
	# - บันทึกข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร
	info = {'brand':{'q':'Brand: ','value':''},
			'color':{'q':'Color: ','value':''},
			'plate':{'q':'Plate: ','value':''},
			'card':{'q':'Card: ','value':''}}
	timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# data = input('Send to Server: ')

	for k,v in info.items():
		d = input(v['q'])
		info[k]['value'] = d

	text = 'in|' # 'in|' is prefix from car-system-in
	print(info)

	for v in info.values():
		text += v['value'] + '|'

	text += timestamp

	print(text)

	writetocsv(text.split('|'))

	# Connect and Send
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(text.encode('utf-8'))
	data_server = server.recv(buffsize).decode('utf-8')
	print('Data from server: ', data_server)
	server.close()
	print('--------------')








'''
[2]-car-system-in.py
	- client-1.py
	(function)
		- บันทึกข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร
		- บันทึกเวลาเข้า
		- ส่งไปหา [1]
		- บันทึกลงใน csv เครื่องตัวเอง
'''