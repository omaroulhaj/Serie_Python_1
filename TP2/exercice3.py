import random


devine=random.randint(1,100)
num=int (input("On va jouer a un petit jeu,je vais générer un nombre entre 1 et 100 et tu vas le devinez en 7 essais ... : "))
for i in range(0,6):
        
    while(num<1 or num>100):
        num=int (input("Oups, vous avez saisi un nombre en dehors de l'intervalle."))
    if(num<devine):
       num=int(input("Oups, Entrez un nombre plus grand ! "))
       continue
    if(num>devine):
       num=int(input("Oups, Entrez un nombre plus petit ! "))
       continue
    if(num==devine):
        print("Bravo ",devine,"est le nombre que j'ai choisit")
        print("Vous l'avez deviné ",i+1," essais")
        break
if num!=devine:
    print("J'ai gagné ,je suis le meilleur,")
    print("Le nombre que j'ai deviné est ",devine)
    print("Au revoir !")
    

   

