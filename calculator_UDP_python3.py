import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 22223)
sock.bind(server_address)

while True:
	data, address = sock.recvfrom(1024)
	unpacker = struct.Struct('I 1s I')
	unpacked_data = unpacker.unpack(data)

	reply = eval(str(unpacked_data[0]) + unpacked_data[1].decode('UTF-8') + str(unpacked_data[2]))

	sock.sendto(str(reply).encode('UTF-8'), address)
sock.close()
