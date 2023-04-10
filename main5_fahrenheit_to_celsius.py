def fahrenheit_to_celsius(farenheid):
    celsius = (farenheid - 32) * 5/9
    return "{:.3f}".format(celsius)

print("Introduce los grados Farenheid: ")
farenheid = int(input())

celsius = fahrenheit_to_celsius(farenheid)
print("La conversión a Celsius nos da: {}".format(celsius))