import socket
import threading 

bind_ip = '199.83.128.42'
bind_port='80'

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',80))
server.listen(5)
print("[*] Listening on %s:%d" % ('199.83.128.42', 80))

#client-handling thread
def handle_client(client_socket):
	#print out what the client sends 
	request = client_socket.recv(1024)
	print(" [*] Received: %s % request)")

while True:
	client, addr = server.accept()
	print(" [*] Accepted connection from %s:%d" % (addr[0],addr[1]))
	#spin up the client thread too handle incoming data. 
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
