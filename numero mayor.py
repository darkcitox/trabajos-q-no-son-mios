num1 = int(input("Escribe el primer número"))
num2 = int(input("Escribe el segundo número"))
num3 = int(input("Escribe el tercer número"))

if (num1 >= num2) and (num1 >= num3):
   nummayor = num1
elif (num2 >= num1) and (num2 >= num3):
   nummayor = num2
else:
   nummayor = num3

print("El número más grande es", nummayor)
