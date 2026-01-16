'''
Não foi utilizado IA.


Questão 2: Contador de Vogais

Escreva uma função em Python chamada contar_vogais que recebe uma única string como argumento. A função deve retornar o número total de vogais (a, e, i, o, u, e suas versões
maiúsculas A, E, I, O, U) presentes nessa string.
Exemplo de uso (para referência):
# Se a entrada for "Python Developer", a saída deve ser 5.
'''



def contar_vogais(texto):

    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in texto:
        if letra in vogais:
            contador += 1
            
    return contador


entrada_usuario = input("Digite uma frase ou palavra para contar as vogais: ")

total = contar_vogais(entrada_usuario)

print(f"A frase digitada contém {total} vogais.")