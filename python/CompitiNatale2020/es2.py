'''
es2:
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a una NIC, 
composto da 6 coppie di cifre esadecimali separate da due punti.
Un esempio di MAC è 02:FF:A5:F2:55:12.
Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.

Andrea Tomatis
'''

import random

def generaMAC():
	codice = ""
	
	listaCaratteri = {i+1 : str(hex(i))[-1].upper() for i in range(16)}
	
	for k in range(6):
		codice += listaCaratteri[random.randint(1,15)] + listaCaratteri[random.randint(1,15)] + ':'
	return codice[:-1]


def main():
	print(generaMAC())

if __name__ == "__main__":
	main()
