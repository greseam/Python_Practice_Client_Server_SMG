##
# - test server
# Sean gregor
#
# this program sets up the "server" that another program will ping to 
##
import socket # adds the socket python library

serversocket = socket.socket( #defines a variable, and creates it as a socket
    socket.AF_INET, socket.SOCK_STREAM  # sends a stream of socks to my laundry bin
)
host = socket.gethostname() #gets the host name

port = 9999 # number to represent a port on this computer

serversocket.bind((host, port)) # binds the host server to a socket

serversocket.listen(5) # allows connections to the server, in this case its max 5

while True: # while existence, do
    
    clientsocket,addr = serversocket.accept() #waits for a connection

    print("Got a connection from %s" % str(addr)) #prints the address that connected

    msg = 'Thank you for connecting' + "\r\n" # nice friendly hello
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()