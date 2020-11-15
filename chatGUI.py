

from tkinter import *
from tkinter import ttk
################NETWORK##################
import socket
import threading
server_ip = '192.168.1.150'
port = 8000
# -*- coding: utf-8 -*-
def Server():
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

		#############
		new_msg = ''
		if data[:3] == 'ALL':
			msgfromserver = data.split('|')
			for m in msgfromserver[-10:]:
				if m != 'ALL':
					new_msg += m + '\n'
			result.set(new_msg)		
			# data = 'ALL-สวัสดี-สบายดีไหม-ok'

		# elif data != '':
		# 	allmsg.append(data)
		# 	msg10 = allmsg[-10:]
		# 	for m in msg10:
		# 		new_msg += m + '\n'
		# 	result.set(new_msg)

		client.send('We received your message'.encode('utf-8'))
		client.close()

def RunServer():
	task = threading.Thread(target=Server)
	task.start()


def SendMessage(data):
	#data = input('Send: ')
	server_ip = '192.168.1.150'
	port = 7500
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((server_ip,port))
	server.send(data.encode('utf-8'))

	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ',data_server)
	server.close()

def RunSendMessage(data):
	task = threading.Thread(target=SendMessage,args=(data,))
	task.start()

################END NETWORK##################

GUI = Tk()
GUI.geometry('800x800')
GUI.title('Chat Program')

FONT = ('Angsana New',25)
result = StringVar()
result.set('----ข้อความ----')
value = StringVar()
F1 = Frame(GUI)
F1.place(x=25,y=600)

global allmsg
allmsg = []

def Send(event=None):
	new_msg = ''
	msg = value.get()
	if msg != '':
		allmsg.append(msg)
		msg10 = allmsg[-10:]
		for m in msg10:
			new_msg += m + '\n'
	else:
		msg10 = allmsg[-10:]
		for m in msg10:
			new_msg += m + '\n'
	value.set('')
	result.set(new_msg)
	RunSendMessage(msg)

L1 = ttk.Label(GUI,textvariable=result,font=FONT)
L1.place(x=50,y=50)

E1 = ttk.Entry(F1,textvariable=value,font=FONT)
E1.grid(row=0,column=0,ipadx=150,ipady=20)
E1.bind('<Return>',Send)
E1.focus()

B1 = ttk.Button(F1,text='Send',command=Send)
B1.grid(row=0,column=1,ipadx=50,ipady=25)


###########RUN SERVER#############
RunServer()

GUI.mainloop()