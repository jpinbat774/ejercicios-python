import math

a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Los lados deben ser positivos.")
elif a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"El área del triángulo es {area:.2f}")
else:
    print("Las longitudes no pueden formar un triángulo.")