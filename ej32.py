n = int(input("Introduce un número entero positivo: "))

if n < 0:
    print("El número no puede ser negativo.")
else:
    a, b = 0, 1
    serie = []

    while a <= n:
        serie.append(a)
        a, b = b, a + b

    print(f"Serie de Fibonacci hasta {n}: {serie}")