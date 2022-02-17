'''
Client in python
'''
import socket as sck

HOST_CLIENT = ('192.168.0.117', 7000)
HOST_SERVER = ('0.0.0.0', 7000)

def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    
    server.bind(HOST_SERVER)
    data, addr = server.recvfrom(7000)
    print(data.decode())
    client.sendto(data, HOST_CLIENT)
    
    server.close()
    client.close()

if __name__ == '__main__':
    main()