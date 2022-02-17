'''
Server in python 
'''
import socket as sck

LOCAL = ('0.0.0.0', 4096)

def main():
    # s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(LOCAL)
    s.listen()
    conn, addr = s.accept()  

    while True:
        data= conn.recvfrom(4096)
        print(data[0].decode())
        conn.sendto(data)

    s.close()

if __name__ == '__main__':
    main()