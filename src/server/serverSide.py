import hashlib
import socket
from threading import Thread
from SocketServer import ThreadingMixIn
from lib.pyQueue import pyQueue
from UserManagement import UserManagement

class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)

        self.ip = ip
        self.port = port

        print "[+] New thread started for " + ip + ":" + str(port)



    def run(self):

        conn.send("Enter Username: ")
        username = conn.recv(BUFFER_SIZE)
        conn.send("Enter Password: ")
        password = conn.recv(BUFFER_SIZE)

        userManag = UserManagement(username, password).authentication()

        while(userManag):
            data = conn.recv(BUFFER_SIZE)
            commandQ.enqueue(data)
            if not data:
                break
            print "received data:", data
            conn.send(data)
        conn.close()

#-----------------------------------------------------------------------------------------------------------------------


TCP_IP = '0.0.0.0'
TCP_PORT = 62
BUFFER_SIZE = 128

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
commandQ = pyQueue()

while True:

    tcpsock.listen(4)
    print "Waiting for incoming connections..."
    (conn, (ip, port)) = tcpsock.accept()
    newThread = ClientThread(ip, port)
    newThread.start()
    threads.append(newThread)


for t in threads:
    t.join()