from socket import *
serverName="192.168.0.101"
serverPort=12000

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

while True:
    message=raw_input('Type message:')

    clientSocket.send(message)
    if message=="exit":
        clientSocket.close()
        exit(0)
    else :
        print "message is sent"

