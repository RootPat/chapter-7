import socket 

target_host='127.0.0.1'
target_port='8008'

client = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
client.connect(('5.56.62.160', 80))
client.send("GET / HTTP/1.1\r\nHost: 5.56.62.160\r\n\r\n")
response = clinet.recv(4096)
print(response)
