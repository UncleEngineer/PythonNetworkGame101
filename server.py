import socket
import select

LEN_HEADER = 10

IP = "192.168.1.150"
PORT = 1234 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((IP,PORT))
server.listen()

server_list = [server]

clients = {}

print(f'Server is listening {IP} : {PORT}')

def recv_msg(client):
	try:
		message_header = client.recv(LEN_HEADER)
		if not len(message_header):
			return False
		message_len = int(message_header.decode('utf-8').strip())
		return {'header':message_header,'data': client.recv(message_len)}

	except:
		return False

while True:
	read_sockets, _, exception_sockets = select.select(server_list, [],server_list)
	for notice in read_sockets:
		if notice == server:
			client , clientaddr = server.accept()
			user = recv_msg(client)
			if user is False:
				continue
			server_list.append(client)
			clients[client] = user
			print('Connection is accepted by {}:{} username:{}'.format(*clientaddr,user['data'].decode('utf-8')))
		else:
			msg = recv_msg(notice)
			if msg is False:
				print('Connection is close from {}'.format(clients[notice]['data'].decode('utf-8')))
				server_list.remove(notice)
				del clients[notice]
				continue
			user = clients[notice]
			print(f"Received message from {user['data'].decode('utf-8')}:{msg['data'].decode('utf-8')}")
			for client in clients:
				if client != notice:
					client.send(user['header'] + user['data'] + msg['header'] + msg['data'])

	for notice in exception_sockets:
		server_list.remove(notice)
		del clients[notice]


