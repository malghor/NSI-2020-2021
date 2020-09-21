from math import *
class Angle():
        
    def __init__(self,angle:int,angle2:int)->int:
        #assert angle<0;"Votre angle doit être supérieur a 0"
        #assert angle2<0;"Votre angle doit être supérieur a 0"
        self.angle=angle%360
        self.angle_radian=self.angle*(pi/180)
        self.angle2=angle2%360
        self.angle2_radian=self.angle2*(pi/180)
        
    def getAngle(self):
        return self.angle
    def getAngle2(self):
        return self.angle2
    
          
    def ajoute(self)->int:
        self.angle_final=(self.angle+self.angle2)%360
        if self.angle_final==0:
            return 360
    
        else:           
            return self.angle_final
        
    def afficher(self):
        print(self.getAngle(),"degrés")
        print(self.ajoute(),"degrés (angle suite à l'ajout)")
        print("cosinus de",self.angle,"°", ":",self.cosinus())
        print("sinus de",self.angle,"°", ":",self.sinus())
        
    def cosinus (self)->int:
        self.resultat=cos(self.angle_radian)
        return round(self.resultat,2)
    def sinus(self)->int:
        self.resultat=sin(self.angle_radian)
        return round(self.resultat,2)
        
            
    
t=Angle(789,180)
#t.afficher()



#----------------------------------------
class Date():
    
    def __init__(self,jour:int,mois:int,année:int)->str:
        self.j=jour
        self.m=mois%12
        self.a=année
    
    def getJ(self):
        return self.j
    def getM(self):
        return self.m
    def getA(self):
        return self.a
    
    def afficher(self):
        mois=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
        print(self.getJ(),mois[self.m-1],self.getA())
        
    def anterieurA(self,d1):
        """
       Retourne True si d1 est est antérieur a d2, sinon renvoie False 
        """
        return self.a<d1.a  or \
            self.a==d1.a and (self.m<d1.m or\
            self.m==d1.m and self.j<d1.j)
        

d1=Date(16,9745,1789)
d2=Date(12,73536,1998)
d1.afficher()
d2.afficher()
print(d1.anterieurA(d2))
        





















