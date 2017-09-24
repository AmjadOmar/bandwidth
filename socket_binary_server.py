import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('isoptera.lcsc.edu', 5001)
sock.bind(server_address)
sock.listen(1)

unpacker = struct.Struct('I 2s f')

while True:
    print('\nwaiting for a connection')
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        print('received "%s"' % binascii.hexlify(data))

        unpacked_data = unpacker.unpack(data)
        print('unpacked:', unpacked_data)
        
    finally:
        connection.close()
