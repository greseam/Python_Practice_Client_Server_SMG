##
# - test server User
# Sean
#
# this program pings the computer and alerts the "server" of a connection
##
import socket # adds the socket python library

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines a variable, and creates it as a socket

host = socket.gethostbyname('10.3.5.29') #gets the host name

port = 9999 #port name

s.connect((host, port)) # binds the host server to a socket

msg = s.recv(1024) # sets the buffer bit rate?



s.close()
print(msg.decode('ascii')) #prints the message