import socket
import struct

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 22223)

values = (int(input()), str(input()).encode('UTF-8'), int(input()))
packer = struct.Struct('I 1s I')
packed_data = packer.pack(*values)

connection.sendto(packed_data, server_address)
data,_ = connection.recvfrom(1024)
print(data.decode('UTF-8'))

connection.close()
