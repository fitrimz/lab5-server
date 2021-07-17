import socket

s = socket.socket()
print("Berjaya buat socket")


s.bind(('192.168.1.27',8888))
print("Berjaya bind socket di port: "+str(8888))

s.listen(5)
print("Socket tengah menunggu client!")

file = open("inputfile.txt","wb") 

while True:
    c, addr = s.accept()
    print("Dapat capaian dari: "+str(addr))
    c.send(b'Terima Kasih!')
    
    RecvFile = c.recv(1024)
    while RecvFile:
        file.write(RecvFile)
        RecvFile = c.recv(1024)
    file.close()
    print("\n File berjaya mendapat salinan file \n")

    c.close()
    break
