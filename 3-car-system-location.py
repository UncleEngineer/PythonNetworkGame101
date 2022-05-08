import socket
from datetime import datetime
############Threading Server##############

plate_dict = {}
# plate_dict = {'1กก99':['312341234',31234234,'13241234']}

import threading
serverip_location = '192.168.0.100'
port_location = 9500
buffsize_location = 4096

def LocationServer():
	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		server.bind((serverip_location,port_location))
		server.listen(1)
		print('waiting client...')

		client, addr = server.accept()
		print('connected from:', addr)

		data = client.recv(buffsize_location).decode('utf-8')
		print('Data from client: ',data)

		# data from 4 : data = 'check|1กง999'
		source = data.split('|')[0] # มาจากโปรแกรมฝั่งไหน? in / location / check
		plate = data.split('|')[1] # '1กง999'

		if source == 'check':
			check = plate_dict[plate] # ['f583f7b5', 'in', 'toyota', 'red', '1A111', '1002', '2022-05-08 11:40:02']
			text = 'location|'
			for c in check:
				text += c + '|'

			client.send(text.encode('utf-8'))
			client.close()
		else:
			client.close()

##########RUN THREAD##########
task = threading.Thread(target=LocationServer)
task.start()

############CSV##############
import csv
def writetocsv(data):
	# data = ['toyota','red','1A11','1001','2022-05-07 15:29:15']
	with open('2-car-system-in.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data) # no s is single line append
	print('csv saved')

############split##############
def splitrow(datalist, columns=7):
    result = []
    buflist = []
    for i,t in enumerate(datalist,start=1):
        if i % columns == 0:
            buflist.append(t)
            # print(buflist)
            result.append(buflist)
            buflist = []
        else:
            buflist.append(t)
    return result

############ADRESS##############
serverip = '192.168.0.100'
port = 9000
buffsize = 4096

while True:
	q = input('[1] - get multiple car information\n[2] - get single car information\n[3] - Save Car Zone\n[q] - exit\n>>> ')
	if q == '1':
		text = 'location|allcar'
	elif q == '2':
		getcar = 'Enter Plate Code: '
		text = 'location|{}'.format(getcar)
	elif q == '3':
		plate = input('Enter Plate Code: ')
		getzone = input('Enter Zone Number: ')
		if len(plate_dict[plate]) == 7:
			# ยังไม่เคยกรอก ข้อมูลจะมีทั้ง 7 รายการ
			plate_dict[plate].append(getzone)
		else:
			# ถ้าเคยกรอกไปแล้ว ต้องการเปลี่ยนให้ใช้แบบนี้
			plate_dict[plate][7] = getzone

	elif q == 'q':
		break
	
	if q != '3':
		# Connect and Send
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		server.connect((serverip,port))
		server.send(text.encode('utf-8'))
		data_server = server.recv(buffsize).decode('utf-8')
		print('Data from server: ', data_server)
		datalist = data_server.split('|')[1:-1] # [1:-1] remove prefix and subfix
		for row in splitrow(datalist,7):
			print(row)
			# ['f583f7b5', 'in', 'toyota', 'red', '1A111', '1002', '2022-05-08 11:40:02']
			if row[4] not in plate_dict:
				plate_dict[row[4]] = row # บันทึกข้อมูลของรถเก็บไว้เป็น dict
		server.close()



'''
[3]-car-system-location.py
	- client-1.py
	(function)
		- ดึงข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร จาก [1]
	- server.py
		- บันทึกตำแหน่งโซนของรถได้
		- ส่งข้อมูลรถไปยัง [4]
'''