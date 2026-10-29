def fattoriale(n):
	risultato = 1
	for numero in range(1, n + 1):
		risultato *= numero
	return risultato


numero = int(input("Inserisci un numero intero non negativo: "))
if numero < 0:
	print("Il numero deve essere non negativo.")
else:
	print(f"Il fattoriale di {numero} è {fattoriale(numero)}")
