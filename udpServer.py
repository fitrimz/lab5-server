import socket


#create udp socket

udpS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("BERJAYA BUAT SOCKET UDP")

udpS.bind(('',8080))

print ("BERJAYA BIND DGN SOKET UDP DI PORT:" +str(8080))

while True:

        #recevive data in UDP via recvfrom

	data, addr =  udpS.recvfrom(1024)
	print(data)
