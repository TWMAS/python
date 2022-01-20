"""Escribe un programa que imprima un número real (float) 
al azar entre 1 y 10 (ambos incluidos). No vayas a cometer el 
error de generar un número aleatorio entre 0 y 10,
 en lugar de hacerlo entre 1 y 10. 
"""
import random
numero = float(random.randrange(1,11))
print (numero)