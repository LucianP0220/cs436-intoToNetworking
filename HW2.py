#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET , SOCK_STREAM)
# Prepare a server socket on a particular port
# Fill in code to set up the port

serverPort = 6789
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve ...')
    connectionSocket, addr = serverSocket.accept() # Fill in code to get a connection
    try:
        message = connectionSocket.recv(1024).decode()# Fill in code to read GET request
        filename = message.split ()[1]
        # Fill in security code
        f = open(filename[1:])
        outputdata = f.read()# Fill in code to read data from the file
        # Send HTTP header line(s) into socket
        # Fill in code to send header(s)
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i]. encode ())
        connectionSocket.send("\r\n".encode ())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/ 1.1 404 File Not Found\r\n\r\n".encode())
        connectionSocket.send(b'<html><head></head><body><h1>404 NotFound</h1></body></html>')
        
        # Fill in
        # Close client socket
        connectionSocket.close()
        # Fill in
serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
