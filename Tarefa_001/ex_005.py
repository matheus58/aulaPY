"""
Escreva um aplicativo que insere um número consistindo em cinco dígitos
do usuário, separa o número em seus dígitos individuais e imprime os
dígitos separados uns dos outros por três espaços cada. Por exemplo, se o
usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.
5. Melhore o programa anterior, permitindo a entrada de números com
quaisquer dígitos.
"""
print("Digite um numero:")
numero = int(input("=> "))
numero_str = str(numero)

for digito in numero_str:
    print(digito, end="   ")
