# -*- coding: utf-8 -*-
from random import *


class Domino:
    def __init__(self,gauche,droite):
        self.droite=droite
        self.gauche=gauche
        
    def getDroite(self):
        return self.droite
    def getGauche(self):
        return self.gauche
    
    
    def nbPoint(self):
        points=self.getDroite+self.getGauche
        return points
        
    def Blanc(self):
        if self.getDroite==0 and self.getGauche==0:      
            self.getDroite=(" ")    
            self.getGauche=(" ") 
        print(self.getGauche,self.getDroite)
    
    
    def Double(self):
        print(self.getGauche,
              """
              """,
              self.getDroite)
            
        
    
        
    def afficher(self):
        if self.getDroite==self.getGauche:
            return self.Double
            return self.nbPoint
        elif self.getDroite==0 and self.getGauche==0:
            return self.Blanc
            return self.nbPoint
        else:
            print(self.getGauche(),self.getDroite())
            
    
d=Domino(0,6)
d.afficher()