"""
Lanzador de monedas: (4 pts)

    Crea un programa que imprima al azar 0 o 1.
    En lugar de 0 o 1, que imprima cara o cruz.
    Añádele un bucle para que lo haga 50 veces.
    Crea una suma acumulada para 
    el total de veces que salió cara y las que salió cruz. 
"""

import random
for i in range (51):
    numero = random.randrange(0,2)
    if (numero == 1):
        print (i,"cara")
    elif (numero == 0):
        print (i,"cruz")