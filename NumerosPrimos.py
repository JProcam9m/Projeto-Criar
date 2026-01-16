'''
Questão 5: Números Primos em um Intervalo

Escreva uma função em Python que recebe um número inteiro N (você pode usar um valor
fixo, como 20) e imprime todos os números primos no intervalo de 1 até N (inclusive N).
Um número primo é um número natural maior que 1 que não pode ser formado pela
multiplicação de dois números naturais menores.

Saída esperada (se N for 20):

2, 3, 5, 7, 11, 13, 17, 19
'''

def imprimir_primos(n):

    for num in range(2, n + 1):
        eh_primo = True  
        

        for i in range(2, num):
            if num % i == 0:    
                eh_primo = False 
                break      
        
        if eh_primo:
            print(num, end=", " if num < 19 else "")


imprimir_primos(20)


