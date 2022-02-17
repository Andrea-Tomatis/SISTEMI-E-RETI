import socket as sck
import threading as thr

connessioni = []

class Client_Manager(thr.Thread):
    def __init__(self, addr, conn):
        thr.Thread.__init__(self)
        self.addr = addr
        self.conn = conn
        self.running = True
    
    def run(self):
        while self.running:
            msg_received = self.conn.recv(4096)
            if msg_received.decode()[:-1] == 'exit': 
                self.running = False
            else:
                print(f'<{thr.current_thread()}>messaggio ricevuto da {self.addr}: {msg_received.decode()}')
                for connection in connessioni:
                    connection.conn.sendall(msg_received)
    

class Accettazione(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s
    
    def run(self):
        while True:
            conn, addr = self.s.accept()
            client = Client_Manager(addr, conn)
            connessioni.append(client)
            client.start()


def main():
    print(thr.current_thread())
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(('127.0.0.1', 5001))
    s.listen()

    acc = Accettazione(s)
    acc.start()

    while True:
        for c in connessioni:
            if not c.running:
                c.conn.close()
                c.join()
                connessioni.remove(c)

if __name__ == "__main__":
    main()