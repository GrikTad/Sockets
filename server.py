import socket

s=socket.socket()
print("Socket has been successfully created.")

port = 1234
s.bind(('',port))
print("Socked has been binded to "+str(port))

s.listen(6)
print("Socket is now listening")

while True:
    sock, client_address = s.accept()
    print("Connected to "+ str(client_address)) 
    sock.send("Thank you for conecting :) ".encode())
    sock.close()