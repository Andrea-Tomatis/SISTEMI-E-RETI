'''
es1:
Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri qualora 
l'utente voglia una password semplice, o di 20 caratteri ascii qualora desideri una password più complicata.

Andrea Tomatis
'''

import random

def generateList(lung):
	listaNum = [str(i) for i in range(10)]
	
	for i in range(ord('a'),ord('z')+1):
		listaNum.append(chr(i))
	
	string = ""
	for k in range(lung):
		car = listaNum[random.randint(0,len(listaNum)-1)]
		string +=  car if random.randint(0,1) else car.upper() 
	return string
	

def main():
	lenght = int(input("insert the password lenght(8 or 20): "))
	if lenght != 8 and lenght != 20:
		raise Exception("error: invalid password lenght")
		
	myPassword = generateList(lenght)
	print(f"your password is: {myPassword}")


if __name__ == "__main__":
	main()
