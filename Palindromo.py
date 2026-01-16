'''
Utilizado IA para confirmar exatamente o que era um palíndromo.


Questão 3: Checador de Palíndromo Básico
Escreva uma função e_palindromo que recebe uma única string (assuma que não há espaços ou pontuação) e retorna True se a string for um palíndromo (lida da mesma forma de trás para frente) e False caso contrário.
Exemplo de uso (para referência):
# "arara" deve retornar True
# "teste" deve retornar False

'''

def e_palindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False

palavra = input('Digite uma palavra: ')

if e_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')