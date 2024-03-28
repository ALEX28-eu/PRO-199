import socket
from threading import Thread

#  socket.socket(socket family, socket type)
# AF_INET represents IPv4 while AF_INET6 represents IPv6
# It is the default value (if not provided) and it
# is used to create a TCP Socket. We could also use SOCK_DGRAM which is used to
# create a UDP Socket
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
clients=[]

ip_address="127.0.0.1"
port=8000

# 127.0.0.1:8000 so we are putting it in 1 bracket then putting inside the bind method
server.bind((ip_address,port))
server.listen()
print("Server is running....")


def clientthread(connection,addr):
    connection.send("Welcome to the chat room!".encode("utf-8"))



# This accept() method accepts any connection request made to the server and returns 2
# parameters -
# 1. The socket object of the client that is trying to connect
# 2. Their IP Address and Port number in the form of a tuple

while True:
    connection,addr=server.accept()
    clients.append(connection)
    print(addr[0]+" connected")
    
    new_thread =Thread(target=clientthread,arg=(connection,addr))
    new_thread.start()


