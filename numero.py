import random
numero = random.randint(1, 10)

intentos = 0
print('Adivina el número del 1 al 10:')

while intentos < 3:
    intento = int(input())
    intentos += 1
    if intento < numero:
        print('Casi, intentalo denuevo')
    if intento > numero:
        print('Casi, intentalo denuevo')
    if intento == numero:
        break
if intento == numero:
    print('Lo lograste ' + str(intentos) + ' intentos')
else:
    print('Casi, el número era ' + str(numero))
