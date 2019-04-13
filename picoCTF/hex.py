#!/usr/bin/env python

import socket
import sys

host = '2018shell.picoctf.com'  # Standard loopback interface address (localhost)
port = 14390        # Port to listen on (non-privileged ports are > 1023)

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address')
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

#Send data
def send(word):
    try:
        s.sendall(word)
    except socket.error:
        print 'Send failed'
        sys.exit()
# Receive data
print('# Receive data from server')
def receive():
    global reply
    reply = s.recv(4096)
    print reply

receive()
first = reply.find('stored.')
last = reply.find('Please')
word = reply[first+8:last-1]+'\n'
send(word)

receive()
first = reply.find('Please give me the')
last = reply.find(' as a')
word = reply[first+19:last]
word = word.decode('HEX') + '\n'
send(word)

receive()
first = reply.find('Please give me the')
last = reply.find(' as a')
word = (reply[first+20:last])
word = list(word.split(' '))
n = ''
for i in word:
    n += chr(int(i,8))

send(n+'\n')
receive()
