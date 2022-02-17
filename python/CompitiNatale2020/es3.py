'''
es3:
Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:
1, 1, 2, 3, 5, 8, 13 (...)
Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata 
dall'utente.

Andrea Tomatis
'''

def trovaNumero(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return trovaNumero(n-1) + trovaNumero(n-2)


def main():
	number = int(input("inserisci il numero della serie: "))
	for i in range(number):
		print(trovaNumero(i))


if __name__ == "__main__":
	main()
