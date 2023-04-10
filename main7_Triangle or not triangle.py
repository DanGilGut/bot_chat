"""Read three angles given on separate input lines
and check whether they form a triangle.
Print the answer in the following format:
"The triangle is valid!" or "The triangle is not valid!"."""

print("Introduce los tres angulos del triángulo: ")

primer_angulo = int(input())
segundo_angulo = int(input())
tercer_angulo = int(input())


def verificacion(primer_angulo, segundo_angulo, tercer_angulo):
    if primer_angulo + segundo_angulo + tercer_angulo == 180:
        resultado = "The triangle is valid!"
    else:
        resultado = "The triangle is not valid!"

    return resultado


print(verificacion(primer_angulo, segundo_angulo, tercer_angulo))
