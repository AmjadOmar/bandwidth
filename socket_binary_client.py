import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('isoptera.lcsc.edu', 5001)
sock.connect(server_address)

values = (1, 'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)

try:
    
    # Send data
    print('sending "%s"' % binascii.hexlify(packed_data), values)
    sock.sendall(packed_data)

finally:
    print('closing socket')
    sock.close()
