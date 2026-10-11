TAE =0.04

capital = (float(input("Introduzca el capital")))


primer_credito = (capital * (1+TAE))
print("En el primer año de inversión su credito es: "+ str(primer_credito))

segundo_credito = (primer_credito * (1 + TAE))
print("En el segundo año de inversión su credito es:" + str(segundo_credito))

tercer_credito = (segundo_credito* (1 + TAE) )
print("En el tercer año de inversion su credito es:" + str(tercer_credito))

print("Tras tres año de inversion su credito es:" + str(round(tercer_credito,2)))

