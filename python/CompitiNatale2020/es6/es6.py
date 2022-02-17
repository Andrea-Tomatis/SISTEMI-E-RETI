'''
es6:
Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 ad oggi, proveniente da varie fonti 
(colonna “Source”). Scrivere un programma che generi un dizionario che abbia come chiave l’anno (“Year”) e valore la media aritmetica delle 
anomalie registrate dalle varie fonti durante quell’anno.
Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) trovi la anomalia massima e minima nel periodo compreso 
tra anno_1 e anno_2.

Andrea Tomatis
'''

def leggiFile(nomefile):
	f = open(nomefile, "r")
	k = 0
	clima = {}
	anno = 0
	ndati = 0
	for line in f:
		stringa = line.split(',')
		
		if stringa[0] == "Source":
			continue
		
		if anno == 0:
			anno = int(stringa[1])
		
		if int(stringa[1]) != anno:
			try:
			    clima[anno] = k/ndati
			except ZeroDivisionError:
			    clima[anno] = 0.0
			k = 0
			ndati = 0
			anno = int(stringa[1])
			
		k += float(stringa[2])	
		ndati = ndati + 1
	
	f.close()
	return clima



def anomalieMassimeMinime(dizionario, anno1, anno2):
	minimo = dizionario[anno1]
	massimo = dizionario[anno1]
	for i in range(anno1, anno2):
		if dizionario[i] < minimo:
			minimo = dizionario[i]
		if dizionario[i] > massimo:
			massimo = dizionario[i]
	print(f"anomalia massima: {massimo}, anomalia minima: {minimo}")



def main():
	clima = leggiFile("annual.csv")
	for element in clima:
		print(f"{element} : {clima[element]}")
		
	anno_1 = int(input("inserisci il primo anno di anomalie: "))
	anno_2 = int(input("inserisci il secondo anno di anomalie: "))
	
	anomalieMassimeMinime(clima, anno_1, anno_2)

if __name__ == "__main__":
	main()
	
