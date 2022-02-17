'''
Andrea Tomatis
'''
import socket as sck
import threading as thr
import random
import time

lstClient = []
countdown = True
end_game = False
start_game = False
N_TURNI = 3

#gestisce i client contenuti in lstClient
class Client_Manager(thr.Thread):
    def __init__(self, addr, conn):
        thr.Thread.__init__(self)
        self.addr = addr
        self.conn = conn
        self.nickname = ''
        self.communicate = False
        self.answer = []
        self.running = True
    
    def run(self):
        while self.running:
            if self.communicate: #se il client puo' rispondere manda la risposta
                msg_received = self.conn.recv(4096)
                msg_received = msg_received.decode()
                print(f'<{thr.current_thread()}>risposta di {self.nickname}: {msg_received}')
                self.answer.append(int(msg_received))
                self.communicate = False
                if self.answer[-1] == extract_number:
                    end_game = True
                    for client in lstClient:
                        client.conn.sendall(f'{self.nickname} hai vinto!'.encode())
                elif self.answer[-1] < extract_number:
                    self.conn.sendall('+'.encode())
                elif self.answer[-1] > extract_number:
                    self.conn.sendall('-'.encode())
        
    
#si occupa dell'iscrizione dei giocatori
class Accettazione(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s
    
    def run(self):
        global start_game
        while True:
            conn, addr = self.s.accept()
            client = Client_Manager(addr, conn)
            nick = client.conn.recv(4096)
            client.nickname = nick.decode()
            #si interrompe se riceve la stringa 'iniziamo'
            if nick.decode().startswith('iniziamo'):
                start_game = True
                conn.sendall('exit'.encode())
                conn.close()
                break
            print('saved new player: ' + nick.decode())
            lstClient.append(client)
            client.start()
            client.conn.sendall(f'benvenuto {nick.decode()}'.encode())

#controlla se tutti i client hanno risposto
def allAnswered():
    for client in lstClient:
       if client.communicate: return False
    return True 


def main():
    global extract_number
    extract_number = random.randint(1,100)
    print(extract_number)
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen()

    acc = Accettazione(s)
    acc.start()

    while not start_game:
        pass
    acc.join()

    #la partita inizia quando tutti i concorrenti sono pronti
    for i in range(N_TURNI):
        for client in lstClient:
            client.conn.sendall(f'turno: {i+1} >>'.encode())
            client.communicate = True

        while not allAnswered():
            pass

        if end_game:
            for client in lstClient:
                client.conn.sendall('exit'.encode())
            break
    
    if not end_game:
        max_val = -1
        winner = None
        for client in lstClient:
            best_ans = -1
            for answer in client.answer:
                if abs(extract_number - best_ans) > abs(extract_number - answer):
                    best_ans = answer
            if abs(extract_number - max_val) > abs(extract_number - answer):
                max_val = answer
                winner = client
        for client in lstClient:
            client.conn.sendall(f'ha vinto {client.nickname} con il numero {max_val}'.encode())
    

    #bonus
    for client in lstClient:
        client.running = False
        client.conn.close()
        client.join()
        s.close()


if __name__ == "__main__":
    main()