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
print(somme(3))