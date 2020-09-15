from turtle import *
def koch(n,longueur):
    speed(0)
    pencolor("black")
    shape("turtle")
    ht()

    if n==0:
        forward(longueur)
    else:
        koch(n-1,longueur/3)
        left(60)
        koch(n-1,longueur/3)
        right(120)
        koch(n-1,longueur/3)
        left(60)
        koch(n-1,longueur/3)
print(koch(3,300))
