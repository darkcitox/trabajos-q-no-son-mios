num1 = int(input("Escribe el primer número"))
num2 = int(input("Escribe el segundo número"))
num3 = int(input("Escribe el tercer número"))

if (num1 >= num2) and (num1 >= num3):
   nromayor = num1
elif (num2 >= num1) and (num2 >= num3):
   nromayor = num2
else:
   nromayor = num3

print("El número más grande es", nromayor)
