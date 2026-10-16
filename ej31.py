import math

n = int(input("Introduce un número entero positivo: "))

if n <= 0:
    print("El número debe ser mayor que 0.")
else:
    divisores = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
                divisores.append(n // i)

    divisores.sort()
    print(f"Los divisores de {n} son: {divisores}")