"""
Escribe un programa en Python que: (3 pts)
    Le pida al usuario siete números
    Imprima la suma total de esos números
    Imprima la cuenta de las entradas positivas, 
    las que sean iguales a cero, y las negativas. Emplea 
    una cadena if, elif, else, en lugar de tres if consecutivos 
"""
total = 0
positiu = 0
for i in range(7):
    nuevo_numero = int(input("Introduce un número: " ))
    total += nuevo_numero
    if (nuevo_numero>0):
            positiu = positiu + 1
print("El total es: ",total)
print("El positius es: ",positiu)

