import socket
import sys
from _thread import start_new_thread

HOST = 'raspberrypi.local' # all availabe interfaces
PORT = 65433 # arbitrary non privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except socket.error as msg:
    print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

s.listen(10)
print("Listening...")

# The code below is what you're looking for ############

def client_thread(conn):
    conn.send('Welcome to the Server. Type messages and press enter to send.\n'.encode())

    while True:
        data = conn.recv(1024)
        if not data:
            break
        #reply = b"OK . . " + data
        print('Received', repr(data))
        conn.sendall(data)
    print("[-] Closed connection")
    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()
