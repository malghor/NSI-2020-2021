class Chrono:
    "une classe pour représenter le temps mesuré en heures, minutes et secondes"
    def __init__(self,h,m,s):
        "le constructeur prend comme arguments temps, minutes et secondes"
        self.heures=h
        self.minutes=m
        self.secondes=s
        
    def afficher(self):
        print (str(self.heures)+"h "
                +str(self.minutes)+"m "
                +str(self.secondes)+"s ")
t=Chrono(21,34,55)
t.afficher()

#print(t)
#print(t.__doc__)
#print(t.__init__.__doc__)


class Dino:
    """
    Une classe pour représenter la longeur, la hauteur, le poid et la vitesse d'un dinosaures
    """
    def __init__(self,l,h,p,s):
        """
        Le constructeur prend en argument la longueur, la hauteur, le poid et la vitesse
        """
        self.taille=l
        self.hauteur=h
        self.poid=p
        self.speed=s
        
    def afficher(self):
        print(str(self.taille)+"m de long; "
              +str(self.hauteur)+"m de haut; "
              +str(self.poid)+" tonne; "
              +str(self.speed)+"km/h ")

triceratops=Dino(9,3,9,32)
tyrex=Dino(13,6,8,27)

triceratops.afficher()
tyrex.afficher()