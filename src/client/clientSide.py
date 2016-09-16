import socket

host = socket.gethostname()
port = 62
BUFFER_SIZE = 128
MESSAGE = raw_input("tcpClientA: Enter Message/ Exter exit:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while MESSAGE != exit:

    tcpClientA.send(MESSAGE)
    data = tcpClientA.recv(BUFFER_SIZE)
    print "Server received data : ", data
    MESSAGE = raw_input("tcpClientA:  Enter message to continue/ Enter exit:")

tcpClientA.close()