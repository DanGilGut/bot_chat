"""
Read the input three times.
Each one contains the age of a person – Jack's, Alex's, and Lana's.
Find the youngest one among them and print this person's age.

jack_age = int(input())
alex_age = int(input())
lana_age = int(input())
"""


jack_age = int(input())
alex_age = int(input())
lana_age = int(input())

lista_edades = [jack_age, alex_age, lana_age]
lista_edades.sort()
print(lista_edades[0])