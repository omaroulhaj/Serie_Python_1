nom=[]
qte=[]
prix_u=[]
S=0

for i in range(0,2):
    nom.append(str(input("Donnez le nom d'article : ")))
    qte.append(int(input(f"Donnez le quantité du {i+1}er d'article : ")))
    prix_u.append(int(input(f"Donnez le prix untaire du {i+1}er d'article : ")))

for i in range(0,2):
    S+=prix_u[i]*qte[i]
    print(f"Totale pour l'article {nom[i]} : {prix_u[i]*qte[i]}(ht)")
print(f"Le totale pour votre article de votre facture est : {S*0.2+S}(TTC)")
