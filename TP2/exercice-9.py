L=[]

print("Veillez saisir quelle type d'opération vous voullez faire : ","1- Tapez 1 si  « euro en dirham (mad) »","2- Tapez 2 si  « dirham en euro (euro) »",sep="\n")
i=int(input(">>> "))
while i!=1 and i!=2 :
    i=int(input("Ooops ,Tapez 1 ou 2 ! : "))
num=1
print("Veuillez saisir autant de valeur que vous voullez. La saisie va s’arrêter dès que vous entrez un nombre négatif.")
while num>0 :
    num=int(input("Entrez : "))
    if num>0:
        L.append(num)
for j in L:
    if i==1:
        print(j," € = {0:.3f}".format(j*10.86),"MAD")
    if i==2:
        print(j," MAD =  {0:.3f}".format(j*0.092),"€")

