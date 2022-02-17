'''
Client in python
'''
import socket as sck
import threading as thr

LOCAL = ('localhost', 5001)

class Connection(thr.Thread):
    def __init__(self, port, s):
        thr.Thread.__init__(self)
        self.port = port
        self.s = s
        self.running = True
    def run(self):
        while self.running:
            data, addr = self.s.recvfrom(self.port)
            print(f"\nmessaggio arrivato: {data.decode()}")

def main():
    #s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(LOCAL)
    conn = Connection(5001, s)
    conn.start()

    while True:
        msg = input('insert a message: ')
        s.sendall(msg.encode())
        if msg == 'exit':
            print('ecco')
            conn.running = False
            conn.join()
            s.close()
            exit()
    

if __name__ == '__main__':
    main()
