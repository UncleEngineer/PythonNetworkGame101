# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import random
###############NETWORK################
import socket
import threading

server_ip = '192.168.1.150'
port = 8000


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

		scoreboard.delete(*scoreboard.get_children()) # Clear Data in Scoreboard and Update new data
		for i,kv in enumerate(allplayer.items()):
			scoreboard.insert('','end',values=(i+1,kv[1]['ip'],kv[1]['name'],0,0))


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
######################################

GUI = Tk()
GUI.geometry('700x650')
GUI.title('StaffGUI')

FONT = ('Angsana New',25)

def Create():
	password = random.randint(1,1000)
	RandomPW.set(str(password).zfill(3))

F1 = Frame(GUI)
F1.pack(pady=50)
F2 = Frame(GUI)
F2.pack() 

buttonStyle = ttk.Style()
buttonStyle.configure('my.TButton',font=FONT)
B1F1 = ttk.Button(F1,text='Create',style='my.TButton',command=Create)
B1F1.grid(row=0,column=0,ipadx=50,ipady=20)

RandomPW = StringVar()
RandomPW.set('Please Click Create to Generate!')


L1F1 = ttk.Label(F1,textvariable=RandomPW,font=FONT)
L1F1.grid(row=0,column=1,padx=20)

B1F2 = ttk.Button(F2,text='START',style='my.TButton')
B1F2.pack(ipadx=50,ipady=20)

scoreboard = ttk.Treeview(F2)
scoreboard.pack(pady=50)

scoreboard['columns'] = ('no','ip','name','total','current',)
scoreboard['show'] = 'headings'

scoreboard.column('no',width=100,anchor='c')
scoreboard.column('ip',width=100,anchor='c')
scoreboard.column('name',width=100,anchor='c')
scoreboard.column('total',width=100,anchor='c')
scoreboard.column('current',width=100,anchor='c')

scoreboard.heading('no',text='No.')
scoreboard.heading('ip',text='IP')
scoreboard.heading('name',text='Name')
scoreboard.heading('total',text='Total')
scoreboard.heading('current',text='Current')

#scoreboard.insert('','end',values=('1','Mr.A',100,20))
RunServer()
GUI.mainloop()