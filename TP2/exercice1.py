valeur=int (input("Donnez un chiffre 1-9 : "))
while(valeur>=10 and valeur==valeur//1):
    valeur=int (input("Donnez un chiffre 1-9 : "))
    
somme=valeur*(1+11+111+1111)
print(f" a={valeur} alors la somme a+aa+aaa+aaaa ={somme}")