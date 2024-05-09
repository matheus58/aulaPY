# Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar ou par.

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print(f"Numero: {numero} e par")
else:
    print(f"Numero: {numero} e ímpar")
