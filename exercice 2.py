from random import*
def devinette(s):
    start=True
    while start :
        x=randint(1,15)
        r=int(input("votre chiffre"))
        if r==x:
            return("Bravo vous avez trouver le bon nombre")
            start = False
        elif r<x:
            return("trop grand")
            r=int(input("votre chiffre"))
            start=True
        elif r>x:
            return("plus petit")
            r=int(input("votre chiffre"))
            start=True

print(devinette(0))


