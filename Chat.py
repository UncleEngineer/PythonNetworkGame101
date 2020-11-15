from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('600x700')

F1 = Frame(GUI)
F1.place(x=15,y=600)

FONT1 = ('Angsana New',25)

v_msg = StringVar()
E1 = ttk.Entry(F1,textvariable=v_msg,font=FONT1,width=40)
E1.grid(row=0,column=0)

global allmsg
allmsg = []

def SendMessage(event=None):
	global linenumber
	linenumber = 0	
	msg = v_msg.get()
	allmessage = ''
	if msg != '':
		allmsg.append(msg)
		msg10 = allmsg[-10:]
		
		for m in msg10:
			allmessage += m + '\n'
	result.set(allmessage)
	v_msg.set('')

B1 = ttk.Button(F1,text='Send',command=SendMessage)
B1.grid(row=0,column=1,padx=10,ipadx=15,ipady=10)

E1.bind('<Return>',SendMessage)
E1.focus()
########text#######

result = StringVar()
result.set('-------ข้อความจะปรากฏที่นี่-------')
L1 = ttk.Label(GUI,textvariable=result,font=FONT1,width=50)
L1.place(x=20,y=20)
############History##############

global linenumber
linenumber = 0

def Uphistory(event=None):
	global linenumber
	print(linenumber)
	allmessage = ''
	linenumber += 1
	msg10 = allmsg[-10 + linenumber:]
	print(msg10)
	for m in msg10:
		allmessage += m + '\n'
	result.set(allmessage)
GUI.bind('<Up>',Uphistory)

GUI.mainloop()