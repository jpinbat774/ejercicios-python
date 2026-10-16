entrada = input("Introduce los productos de la cesta, separados por comas: ")

productos = entrada.split(",")

for producto in productos:
    print(producto.strip())