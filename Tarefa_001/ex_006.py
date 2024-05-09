"""
Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do
segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.
"""
import math


def calcular_raizes(a, b, c):
    # Calculando o discriminante
    delta = b**2 - 4 * a * c

    # Verificando se o discriminante é negativo (raízes complexas)
    if delta < 0:
        return None, None

    # Calculando as raízes
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2


# Recebendo os coeficientes a, b e c
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calculando as raízes
x1, x2 = calcular_raizes(a, b, c)

# Imprimindo as raízes
if x1 is None:
    print("A equação não possui raízes reais.")
else:
    print("Raiz x':", x1)
    print("Raiz x'':", x2)
