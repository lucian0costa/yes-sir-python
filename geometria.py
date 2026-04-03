import math

valorA, valorB, valorC = float(input()), float(input()), float(input())
area_triangulo_retangulo = (valorA * valorC)/2
area_circulo = valorC ** 2 * math.pi
area_trapezio = ((valorA + valorB) * valorC)/2
area_quadrado = valorB ** 2
area_retangulo = valorA * valorB

print(
    f"Triangulo: {area_triangulo_retangulo:.2f}\n"
    f"Circulo: {area_circulo:.2f}\n"
    f"Trapezio: {area_trapezio:.2f}\n"
    f"Quadrado: {area_quadrado:.2f}\n"
    f"Retangulo: {area_retangulo:.2f}"
)