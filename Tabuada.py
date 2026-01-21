'''
Utilizado Inteligência artificial somente na parte para saber que tipo de conta deveria ser 
utilizada para descobrir se tal número é primo.
'''

def eh_primo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gerar_tabuada(n):
    print(f"\n--- Tabuada do {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

while True:
    try:
        entrada = input('\nDigite um número inteiro (ou a letra S para sair): ').strip()
        
       
        if entrada.lower().startswith("s"):
            print("Saindo...")
            break
            
        numero = int(entrada)

        if eh_primo(numero):
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")

        gerar_tabuada(numero)
        break

    except ValueError:
        print("Por favor, digite apenas números inteiros.")