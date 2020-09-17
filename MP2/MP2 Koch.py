# -*- coding: utf-8 -*-
from turtle import *
def koch(n,longueur):
    speed(0)
    pencolor("red")
    
    

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
#print(koch(3,300))

def flocon(n, longueur) :
	for i in range(3) :
		koch( n,longueur)
		right(120)
        
flocon(3,300)
    