import random
number = random.randint(1, 10)

number_of_guesses = 0
print('Adivina el número del 1 al 10:')

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Casi, intentalo denuevo')
    if guess > number:
        print('Casi, intentalo denuevo')
    if guess == number:
        break
if guess == number:
    print('Lo lograste ' + str(number_of_guesses) + ' intentos')
else:
    print('Casi, el número era ' + str(number))
