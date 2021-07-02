texto = input("Escribe algo y contaré las letras")


def letras(texto):
    lcount = 0
    for c in texto:
        if c.isalpha():
            lcount += 1
    return lcount


letters = letras(texto)

print("Cantidad de letras : ", letters)
