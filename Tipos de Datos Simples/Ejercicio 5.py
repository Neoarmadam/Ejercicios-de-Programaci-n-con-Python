#Ejercicio 5. Neo Armada.

#Escribir un programa que pregunte al usuario por el 
# número de horas trabajadas y el coste por hora. Después 
# debe mostrar por pantalla la paga que le corresponde.

coste=float(input("Coste por horas: "))
horas=float(input("Horas trabajadas: "))
paga = horas * coste
print("Tienes que cobrar ", paga ,"€.")