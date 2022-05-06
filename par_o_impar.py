"""

Ricardo Curiel. 

Pedir un numero y verificar si es par o impar.

"""

salir = 'a'

while(salir != 's'):

    numero = int(input("Hola, ingrese un número por favor."))

    if(numero % 2 == 0):
        print("El número es par")
    else:
        print("El número es impar")
        
    salir = input("para salir presione s(salir), sino Enter")

