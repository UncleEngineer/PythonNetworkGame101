from tkinter import *
from tkinter import ttk
import random
###############NETWORK################
import socket
import threading
def SendMessage(data):
	#data = input('Send: ')
	server_ip = '192.168.1.150'
	port = 8000
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

def PopupName():
	GUI2 = Toplevel()
	GUI2.attributes('-topmost',True)
	GUI2.geometry('300x250')
	GUI2.title('Name')
	### ช่องกรอก 1 ช่อง
	L = ttk.Label(GUI2,text='Name').pack()
	v_name = StringVar()
	EName = ttk.Entry(GUI2,textvariable=v_name,font=('Angsana New',20))
	EName.pack(pady=10)

	L = ttk.Label(GUI2,text='Room Code').pack()
	v_code = StringVar()
	ECode = ttk.Entry(GUI2,textvariable=v_code,font=('Angsana New',20))
	ECode.pack(pady=10)


	def EnterGame():
		name = v_name.get()
		code = v_code.get()
		v_username.set(name)
		v_codenumber.set(code)
		RunSendMessage('START|{}|{}'.format(code,name))
		GUI2.withdraw()

	B1 = ttk.Button(GUI2,text='Enter Game',command=EnterGame)
	B1.pack(ipadx=20,ipady=10)

	GUI2.mainloop()


GUI = Tk()
GUI.geometry('700x800')
GUI.title('PlayerGUI')

FONT = ('Angsana New',25)

buttonStyle = ttk.Style()
buttonStyle.configure('my.TButton',font=FONT)

######NAME#######
v_username = StringVar()
LName = ttk.Label(GUI,textvariable=v_username,font=FONT)
LName.place(x=30,y=30)

v_codenumber = StringVar()
LCode = ttk.Label(GUI,textvariable=v_codenumber,font=FONT)
LCode.place(x=30,y=70)

######SCORE#######
L1 = ttk.Label(GUI,text='Current Score',font=FONT)
L1.pack(pady=30)

point = StringVar()
point.set('Point')

L11 = ttk.Label(GUI,textvariable=point,font=FONT)
L11.pack()


######BUTTON FIGHT#######
B1 = ttk.Button(GUI,text='Fight',style='my.TButton')
B1.pack(pady=50)

L2 = ttk.Label(GUI,text='Total Score',font=FONT)
L2.pack(pady=30)

sumpoint = StringVar()
sumpoint.set('Sumpoint')

L21 = ttk.Label(GUI,textvariable=sumpoint,font=FONT)
L21.pack()

scoreboard = ttk.Treeview(GUI)
scoreboard.pack(pady=50)

scoreboard['columns'] = ('no','total')
scoreboard['show'] = 'headings'

scoreboard.column('no',width=100,anchor='c')
scoreboard.column('total',width=100,anchor='c')

scoreboard.heading('no',text='No.')
scoreboard.heading('total',text='Total')

scoreboard.insert('','end',values=('1',100))
scoreboard.insert('','end',values=('2',100))
scoreboard.insert('','end',values=('3',100))


PopupName()

GUI.mainloop()