precio_barrapanhoy = 3.49

descuento_nofresco = 0.6

cant_barras_nofreca = int(input("Introduzca la cantidad de barras no frescas"))

precio_barra_nofresca = (precio_barrapanhoy*(1-descuento_nofresco))

print("Precio de pan de hoy:" + str(precio_barrapanhoy))
print("El descuento de pan no fresco es del 60% ") 
precio_final = (precio_barra_nofresca * cant_barras_nofreca)
print("El precio final es:" + str(round(precio_final,2)))

      
      