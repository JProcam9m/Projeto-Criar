
''' 
Neste exercício não foi utilizado Inteligência artificial

Questão 4: Filtragem de Lista
Dada a lista de números: numeros = [12, 5, 23, 8, 17, 40, 3, 30].
Escreva um script que usa um loop for para iterar sobre essa lista e crie uma nova lista
chamada filtrados. Essa nova lista deve conter apenas os números da lista original que
atendem a duas condições:
1. O número é maior que 15.
2. O número é divisível por 2 (par).
Saída esperada (a lista final): [40, 30]

'''


numeros = [12, 5, 23, 8, 17, 40, 3, 30]

filtrados = []

for numero in numeros:
    if numero > 15 and numero % 2 == 0:
        filtrados.append(numero)
        lista_final = (filtrados)

print(lista_final)

        