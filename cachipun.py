import random

def jugar():
    yo = input("piedra, papel o tijera\n")
    yo = yo.lower()

    pc = random.choice(['piedra', 'papel', 'tijera'])

    if yo == pc:
        return "empate, elijieron {}".format(yo, pc)

    if ganar(yo, pc):
        return "ganaste, {} le gana a {}".format(yo, pc)

    return "perdiste, {} no le gana a {}".format(yo, pc)

def ganar(jugador, oponente):
    if (jugador == 'piedra' and oponente == 'tijera') or (jugador == 'tijera' and oponente == 'papel') or (jugador == 'papel' and oponente == 'piedra'):
        return True
    return False

if __name__ == '__main__':
    print(jugar())
