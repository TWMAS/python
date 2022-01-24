"""
Escribe un programa para jugar a piedra, tijera, papel: (4 pts)

    Crea un programa que imprima aleatoriamente 0, 1, o 2.
    Usando sentencias if, expande el programa de manera que 
    ahora imprima al azar piedra, papel o tijera. No hagas la 
    selección desde una lista, tal como hemos visto en el capítulo.
    Añade al programa la opción de que primero le pregunte al 
    usuario qué es lo que elige.
    (Sería más fácil darle a escoger entre las opciones 1, 2, o 3.)
    Añade una declaración condicional para determinar quién gana. 
"""



import random

x=random.randrange(0,3)

j=int(input("introd piedra=0 tijeras=2 o papel=1"))
if (j == 0):
        print ("piedra")
elif (j == 1):
        print ("paper")
if (j == 2):
        print ("tijera")
"""
if (x==0 and j==0):
        print ("empat")
"""
if (x==j):
        print ("empat")

if (x==0 and j==1) or (x==1 and j==2) or (x==2 and j==0):
        print ("gana jugador")


if (x==0 and j==2) or (x==1 and j==0) or (x==2 and j==1):
        print ("perds")

if (x==0):
        print (x, "és piedra")
if (x==1):
        print (x, "és papel")
if (x==2):
        print (x, "és tijera")


 