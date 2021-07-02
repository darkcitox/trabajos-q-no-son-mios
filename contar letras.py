string = input("Escribe el número")

def letras(string):
    lcount = 0
    for c in string:
        if c.isalpha():
            lcount+=1
    return lcount

letters = letras(string)

print("Cantidad de letras : ", letters)
