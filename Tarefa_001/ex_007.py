"""
Escreva um programa que leia a quantidade em segundos e imprima o
resultado em dias, horas, minutos e segundos.
"""

print("********** Conversor de segundos (dias, horas , minutos)************ ")
print("digite o segundos a serem convertidos : ")
entrada_em_segundos = int(input("=>"))


minutos = entrada_em_segundos / 60
horas = minutos / 60
dias = horas / 24

print(f"segundos = {entrada_em_segundos} \nminutos = {minutos}\nhoras = {horas}\ndias = {dias}")
