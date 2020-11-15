import socket
import select
import errno
import sys

LEN_HEADER = 10

IP = "192.168.1.150"
PORT = 1234 

user = input('Please Enter Username: ')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((IP,PORT))
client.setblocking(False)

username = user.encode('utf-8')
username_header = f'{len(username):<{LEN_HEADER}}'.encode('utf-8')
client.send(username_header+username)

while True:
	msg = input(f'{user} > ')
	if msg:
		msg = msg.encode('utf-8')
		msg_header = f'{len(msg):<{LEN_HEADER}}'.encode('utf-8')
		client.send(msg_header+msg)
	try:
		while True:
			username_header = client.recv(LEN_HEADER)
			if not len(username_header):
				print('Connection is closed from server')
				sys.exit()

			username_len = int(username_header.decode('utf-8').strip())
			user = client.recv(username_len).decode('utf-8')
			msg_header = client.recv(LEN_HEADER)
			msg_len = int(msg_header.decode('utf-8').strip())
			msg = client.recv(msg_len).decode('utf-8')
			print(f"{username.decode('utf-8')} > {msg}")

	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Please read this error: {}'.format(str(e)))
			sys.exit()
		continue

	except Exception as e:
		print('Please read this error: {}'.format(str(e))) 
		sys.exit()