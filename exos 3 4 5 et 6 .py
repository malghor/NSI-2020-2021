from math import  *
#
#N=int(input("taille de votre sapin : "))
def sapin(x:int)->int:
    if x!= 0:
        print(x*' '+((N-x)*2+1)*'^')
        sapin(x-1)

#sapin(N)

#-------------------------------------------

def HT (z:int)->int:
    n=1
    while n!=0:
        ttc=z*1.20
        print("Le prix TTC de",z,"€","est de :",ttc,"€")
        n=int(input("pour arreter le script taper 0, sinon taper un autre prix HT pour avoir son prix TTC : "))
        if n==0:
            print("le script est terminer")
        while n!=0:
            print("le prix TTC est de : ", n*1.20,"€")
            n=int(input("pour arreter le script taper 0, sinon taper un autre prix HT pour avoir son prix TTC : "))

#print(HT(50))

#-------------------------------------------
#p=int(input("nombre de poule tué par le chasseur : "))
#c=int(input("nombre de chien tué par le chasseur : "))
#v=int(input("nombre de vache tué par le chasseur : "))
#a=int(input("nombre d' ami tué par le chasseur : "))
z=100
def amende(p:int,c:int,v:int,a:int,z:int)->int:
    z=z-(p*1+c*3+v*5+a*10)
    if z >0:
        print("il reste ",z,"points au chasseur, il n'a donc pas perdu son permis")
    elif z<0 :
        print("Le chasseur a perdu",-z,"points","il a donc perdu son permis",(z/-100),"fois, il doit donc payer",ceil(((z/-100)*200-((z/-100)%1)*200)),"€ d'amende")
    elif z==0:
        print("Le chasseur a perdu 100 points, il doit donc payer  200 € d'ammende")
#
#print(amende(p,c,v,a,z))


#-------------------------------------------

poid=int(input("Votre poid (en gramme) : "))
nourriture=int(input("la quantité de nourriture que vous mangez (en grammes) : "))
x=int(input("nombres d'animaux à  comparer : "))
ratio=(nourriture/poid)
lst=[]

def Haruhi(x:int,ratio:int,lst:list)->int:
    for i in range (x):
        i=int(input("poid de l'animal : "))
        t=int(input("quantité de nourriture que l'animal mange (en grammes) : "))
        ratio_animal=t/i
        if ratio_animal>ratio:
            lst.append(i)
    print ("Le nombre d'animaux mangeant plus qu'Haruhi est de : ",len(lst))
print(Haruhi(x,ratio,lst))

    


#-------------------------------------------










































