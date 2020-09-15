# -*- coding: utf-8 -*-
from random import *


class Domino:
    def __init__(self,droite,gauche):
        self.droite=droite
        self.gauche=gauche
        
    def getDroite(self):
        return self.droite
    def getGauche(self):
        return self.gauche
    
    
    def nbPoint(self):
        self.droite=self.droite
        self.gauche=self.gauche
        
        
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
        elif self.getDroite==0 and self.getGauche==0:
            return self.Blanc
        else:
            print(self.getGauche,self.getDroite)
        
    
d=Domino(1,5)
d.afficher()