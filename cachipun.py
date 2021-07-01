import random

def play():
    yo = input("piedra, papel o tijera\n")
    yo = yo.lower()

    pc = random.choice(['piedra', 'papel', 'tijera'])

    if yo == pc:
        return "empate, elijieron {}".format(yo, pc)

    if is_win(yo, pc):
        return "ganaste, {} le gana a {}".format(yo, pc)

    return "perdiste, {} le gana a {}".format(yo, pc)

def is_win(jugador, oponente):
    if (jugador == 'piedra' and oponente == 'tijera') or (jugador == 'tijera' and oponente == 'papel') or (jugador == 'papel' and oponente == 'piedra'):
        return True
    return False

if __name__ == '__main__':
    print(play())
