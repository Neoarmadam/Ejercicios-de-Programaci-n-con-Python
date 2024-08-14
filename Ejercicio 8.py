#Ejercicio 8. Neo Armada.

#Escribir un programa que pida al usuario dos números 
# enteros y muestre por pantalla la <n> entre <m> da un 
# cociente <c> y un resto <r> donde <n> y <m> son los números 
# introducidos por el usuario, y <c> y <r> son el cociente y 
# el resto de la división entera respectivamente.

n=int(input("Dame el primer numero: "))
m=int(input("Dame el segundo numero: "))
print("El cociente es: ", int(n/m))
print("El resto es: ", int(n%m))