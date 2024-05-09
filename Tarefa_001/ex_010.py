"""
Escreva um programa que leia um número e verifique se é ou não um
número primo
"""
print("**********Digite um numero **********")
numero = int(input(" => "))
if numero > 1:
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        print(f"O número {numero} é um número primo.")
    else:
        print(f"O número {numero} não é um número primo.")
else:
    print("Números menores ou iguais a 1 não são considerados primos.")
