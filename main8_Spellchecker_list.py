dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
palabra = input()
resultado = "Incorrect"

for palabra_diccionario in dictionary:
    if palabra == palabra_diccionario:
        resultado = "Correct"

print(resultado)