nb1=int(input("Saisir le première nombre  : "))
nb2=int(input("Saisir le deuxième nombre  : "))
if((nb1>0 and nb2>0)or(nb1<0 and nb2<0)):
    print("Leur produit est positif")
else: 
    print("Leur produit est négatif")
