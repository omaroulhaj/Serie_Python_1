L=[20,100,2,9,-9,180,57,200,2,9,-9,20,-9,60,71,-9,-9,-9,20]
b=int(input("Veuillez saisir un nombre pour savoir leur occeurences : "))
print("Les occurrences de ",b,"sont :")
n=0
for i in range(len(L)):
    if b==L[i]:
        n+=1
        print("une occurence en position i = ",i)
print("le nombre d'occurence de nombre ",b,"est total=",n)
