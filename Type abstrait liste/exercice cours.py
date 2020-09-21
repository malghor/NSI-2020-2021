class Maillon():
    def __init__(self,valeur=None):
        self.val=valeur
        self.suiv=None
        


class listeChaine():
    def __init__ (self):
        self.tete=None        
       
    def estVide(self):
        if self.tete==None:
            return True
        else:
            return False
            
    def taille(self)->int:
        z=1
        m=self.tete
        while m.suiv is not None:
            m=m.suiv
            z+=1
        return z
    
    def getDernierMaillon(self):
        m=self.tete
        while m.suiv is not None:
            m=m.suiv
            y=m.val
        return y
        

L=listeChaine()
M1,M2,M3= Maillon(5),Maillon(8),Maillon(11)        
L.tete=M1
M1.suiv=M2
M2.suiv=M3
                
#print(L.estVide())
print(L.taille())
print(L.getDernierMaillon())
    