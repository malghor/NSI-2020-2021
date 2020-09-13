from turtle import *
def somme(n:int)->int:
    """
    Cette fonction permet de calculer la somme des chiffres de n entier : exemple de n=3 -> 6
    
    Cette fonction demande un entier et retourne un entier  
    """
    assert type(n)==int, "n doit être un entier"
    assert n>1, "n doit être superieur à 0"
    S=0
    for i in range(1,n+1):
        S+=i
    return(S)
#print(somme(3))

#-------------------------------------------

def somme2(n:int)->int:
    if n==0:
        return 0
    else :
        return n+somme(n-1)
        
#print(somme2(2955))
#-------------------------------------------
def fact(n:int)->int:
    """
    Cette fonction renvoie de résultat de factoriel n
    """
    assert type(n)==int ,"n doit être une entier"
    
    if n==0:
        return 1
    else:
        return n*fact(n-1) 
#print(fact(5))

def fact2(n:int)->int:
    S=1
    for i in range (1,n+1):
        S=S*i
    return S

#print(fact2(5))
#-------------------------------------------

def boucle(i:int,k:int)->int:  
    assert type(i)==int, "i doit être un entier"
    assert type(i)==int ,"k doit être un entier" 
    if i==k:
        print(i)
    else:
        print(i)
        boucle(i+1,k)
        
    return    
    
#print(boucle(0,3))

def boucle2(i:int,k:int)->int:
    for i in range (i,k):
        s=i
        print(s)
        s=i+1
        
#print(boucle2(0,6))

#-------------------------------------------

def fibo(n:int)->int:
    a=0
    b=1
    u=0
    for i in range (n-1):
        u=a+b
        a=b
        b=u
    return u
print(fibo(7))
        
#------------------------------------------- 

        
    
def fibo_rec(n:int)->int:
    """
    Cette fonction permet de calculer le résultat selon le rang de suite la fibonacci 
    """
    assert type(n)==int,"n doit être une entier"
    if n==0:
        return 0
    elif n==1:
        return 1
        
    else:       
        return fibo_rec(n-1)+fibo_rec(n-2)  

print(fibo_rec(7))
        

#------------------------------------------
    
def russe(x:int,y:int)->int:
    """
    Cette fonction permet de calculer la multiplication de deux entier
    """
    assert type(x)== int,"x doit être un entier"
    assert type(y)== int,"y doit être un entier"
    if x==0:
        return 0
    elif x % 2 == 0:
        return russe(x//2 , y+y)
    else:
        return russe(x//2 , y+y) + y

#print(russe(105,253))




    
    
    
    
    
    