import socket 
import os 

#set the host you would like to listen on 
host = '127.0.0.1'
#create a raw scket and bind it to the public interface
if os.name == "nt":
	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind(('127.0.0.1',0))

#we want the IP header sincluded in the capture 
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

#Only applicable if using windows then we need to send an IOCTL
#to set up promiscuous mode 
if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCALL, socket.RCALL_ON)

# read in a single packet
print (sniffer.recvfrom(65565))

#if using windows, turn off promiscuous mode 
if os.name == "nt":
	sniffer.ioctl9(socket.SIO_RCVALL, socket.RCVALL_OFF)

