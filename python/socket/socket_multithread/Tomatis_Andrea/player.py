'''
Andrea Tomatis
'''
import socket as sck
import threading as thr

LOCAL = ('127.0.0.1', 5000)
            

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(LOCAL)

    name = input('what is your nickname: ')
    s.sendall(name.encode())
    if name == 'iniziamo':
        s.close()
        exit()
    print(s.recv(4096).decode())

    while True:
        data = s.recv(4096)
        if data.decode() == 'exit':
            s.close
            break
        msg = input(f"\nmessaggio arrivato dal banco: {data.decode()}")
        try:
            if int(msg) <= 100 and int(msg) >= 0:
                s.sendall(msg.encode())
        except:
            s.sendall('-1'.encode())
        print(s.recv(4096).decode())
    

if __name__ == '__main__':
    main()
