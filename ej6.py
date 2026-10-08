precio_total =  float (input ("Introduzca el precio total"))

IVA = 0.1

precio_producto = (precio_total * (1 - IVA))
precio_IVA= (IVA * precio_total)

print("Ha pagado de IVA :" + str(precio_IVA))

print("El producto cuesta" +str(precio_producto))
