frase = input("Inserisci: ")

nuova_frase = ""
for i in range(len(frase)):
    if i % 2 ==  0:
        nuova_frase += frase[i].upper()
    else:
        nuova_frase += frase[i]

print(nuova_frase)

