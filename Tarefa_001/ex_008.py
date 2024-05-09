"""
Escreva um programa que converta uma temperatura digitada em "C” em
“F”.
"""

print("*************** Conversor de temperatura ****************")
print("<!-- Digite a temperatura e Grau Celsius --!>")
grau_C = float(input("=>"))

grau_F = 9 / 5 * grau_C + 32

print(f"Grau Celsius = {grau_C} \nGrau Farenheits = {grau_F}")
