import math

n = int(input("Introduce un número entero: "))

if n < 2:
    print(f"{n} no es primo.")
else:
    es_primo = True
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{n} es primo.")
    else:
        print(f"{n} no es primo.")