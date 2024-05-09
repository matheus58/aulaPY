"""
Escreva um aplicativo que insere um número consistindo em cinco dígitos
do usuário, separa o número em seus dígitos individuais e imprime os
dígitos separados uns dos outros por três espaços cada. Por exemplo, se o
usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.
"""
print("Digite um numero com 5 digitos")

while True:
    numero = input("=> ")

    if (
        len(numero) == 5 and numero.isdigit()
    ):  # Verifica se a entrada possui 5 dígitos e são todos números
        for digito in numero:
            print(digito, end=" ")
        break
