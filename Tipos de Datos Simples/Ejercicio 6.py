#Ejercicio 6. Neo Armada.

#Escribir un programa que lea un entero positivo,n,
#  introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta n. La suma de 
# los n primeros enteros positivos puede ser calculada de la 
# siguiente forma:

resultado=int(0)
entero=int(input("Dame un numero positivo bb: "))
while entero<1:
    entero=int(input("He dicho un numero positivo tonto: "))
for f in range(1, entero+1):
    resultado+=f
    print("Mondongo: ",f)
print("La suma de los numeros es: ",resultado)