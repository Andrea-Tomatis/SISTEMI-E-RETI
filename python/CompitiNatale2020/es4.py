'''
es4:
Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 15 posizioni 
più avanti nell'alfabeto. Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata 
precedentemente codificata.

Andrea Tomatis
'''

rot15 = {'a' : 'p', 
		 'b' : 'q', 
		 'c': 'r', 
		 'd' : 's',
		 'e' : 't',
		 'f' : 'u',
		 'g' : 'v',
		 'h' : 'w',
		 'i' : 'x',
		 'j' : 'y',
		 'k' : 'z',
		 'l' : 'a',
		 'm' : 'b',
		 'n' : 'c',
		 'o' : 'd',
		 'p' : 'e',
		 'q' : 'f',
		 'r' : 'g',
		 's' : 'h',
		 't' : 'i',
		 'u' : 'j',
		 'w' : 'k',
		 'x' : 'l',
		 'y' : 'm',
		 'z' : 'o'}


def cripta(stringa):
	new_string = ""
	for i in range(len(stringa)):
		new_string += rot15[stringa[i].lower()]
	return new_string
	
def getKey(val):
   for key, value in rot15.items():
      if val == value:
         return key
	
def decripta(stringa):
	new_string = ""
	for i in range(len(stringa)):
		new_string += getKey(stringa[i].lower())
	return new_string
	
	
def main():
	stringa1 = "hello"
	stringa2 = "wtaad"
	print(f"Hello = {cripta(stringa1)}, wtaad = {decripta(stringa2)}") 

if __name__ == "__main__":
	main()
