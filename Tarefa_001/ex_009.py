"""
Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
escolhida. Repita até que a opção saída seja escolhida
"""

while True:
    resposta = int(
        input(
            "(menu):\n \tadição(1)\n \tsubtração(2)\n \tdivisão(3)\n \tmultiplicação(4)\n \tsair(0)\n =>"
        )
    )

    if resposta >= 0 and resposta <= 4:
        if resposta == 1:
            x = int(input(" Digite um numero : \n"))
            y = int(input("Digite outro numero : \n "))
            adição = x + y
            print(f"A soma : \n \t {x}+{y}={adição}")
        if resposta == 2:
            x = int(input(" Digite um numero : \n"))
            y = int(input("Digite outro numero : \n "))
            sub = x - y
            print(f"A soma :\n \t {x}-{y}={sub}")

        if resposta == 3:
            x = int(input(" Digite um numero : \n"))
            y = int(input("Digite outro numero : \n "))
            div = x / y
            print(f"A divisao : \n \t {x}%{y}={div}")
        if resposta == 4:
            x = int(input(" Digite um numero : \n"))
            for numero in range(1, 11):
                print(f"{x} X {numero} = {numero * x}")
        if resposta == 0:
            break
