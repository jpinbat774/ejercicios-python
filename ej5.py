importe_articulo = float (input ("Introduzca el importe del artículo"))

IVA = float (input("Introduzca el porcentaje del IVA (entre 0 y 1)"))

importe_total = (importe_articulo * (1+IVA) )          
print ("Su importe total es"+ str(importe_total))
