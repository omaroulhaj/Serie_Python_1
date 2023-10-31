import math


def delta(a,b,c):
    return b*b-4*a*c
def NombreRacine(a,b,c):
    if delta(a,b,c)==0:
        return 1
    elif delta(a,b,c)>0 :
        return 2
    else :
        return 0

def AfficheNombreRacine(a,b,c):
    if NombreRacine(a,b,c)<0:
        print("L'equation n'admet pas du solution")
    else :
        print("Nombre du racine : ",NombreRacine(a,b,c))

def Racine1(a,b,c):
    return (-b+math.sqrt(delta(a,b,c)))/2*a

def Racine2(a,b,c):
    return (-b-math.sqrt(delta(a,b,c)))/2*a

print("Exemple : x^2-3x+2")
print("Delta = ",delta(1,-3,2))
AfficheNombreRacine(1,-3,2)
if delta(1,-3,2)<0:
    print("")
elif delta(1,-3,2)>0:
    print("Les racines sont S={",Racine1(1,-3,2),",",Racine2(1,-3,2),"}")
else:
    print("Le racine est S={",Racine1(1,-3,2),"}")
