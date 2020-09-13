from math import *
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
#t=Chrono(21,34,55)
#t.afficher()

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
        self.longueur=l
        self.hauteur=h
        self.poid=p
        self.speed=s
        
    def afficher(self):
        print(str(self.longueur)+"m de long ; "
              +str(self.hauteur)+"m de haut ; "
              +str(self.poid)+"tonne(s) ; "
              +str(self.speed)+"km/h ")

    def getLongueur(self)->int:
        return self.longueur
    

triceratops=Dino(9,3,9,32)
tyrex=Dino(13,6,8,27)

triceratops.getLongueur()
#tyrex.afficher()




class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rho=self.calculRho()
        self.theta=self.calculTheta()
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    
    
      
    def calculTheta(self)->int:
        if self.x>0:
            return atan(self.y,self.x)
        elif self.x<0 and self.y>=0 :
            return atan((self.y,self.x)+pi)
        elif self.x<0 and self.y<0:
            return atan((self.y,self.x)-pi)
        elif self.x==0 and self.y>0:
            return pi/2
        elif self.x==0 and self.y==0:
            return (-(pi)/2)
        elif self.x==0 and self.y==0:
            return 0

    def calculRho(self):
        sqrt(self.x**2+self.y**2)
  
    def getTheta(self):
        return self.theta
    def getRho(self):
        return self.rho
    def afficher(self):
        print()
    
    
        
point1=Point(-2,5)
print(point1.getRho())
print(point1.getTheta())
print(point1.getX())
print(point1.getY())

        
    
    
        









