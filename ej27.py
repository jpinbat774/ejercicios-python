nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))

coste_total = precio * unidades

print(f"{nombre} {precio:09.2f} {unidades:03d} {coste_total:011.2f}")