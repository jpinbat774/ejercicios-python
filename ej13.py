num1 =  int(input("Introduce un número"))
num2 =  int(input("Introduce otro número"))

if num2 == 0:
    print("No se puede dividir entre 0")
else:
    c= num1 // num2
    r= num1 % num2 
    
    print (("EL cociente es" +str(c) + "y el resto es" +str(r)))
    