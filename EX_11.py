print("Ce programme calcule l'indice de masse corporelle (IMC) ")
poids=float(input("Donnez votre poids (KG) : "))
taille=float(input("Donnez votre taille (cm) : "))
taille/=100 #pour convertir la taille en cm à m
imc=poids/(taille*taille)
print(f"Votre IMC = {imc}")
if imc>40:
    print("IMC : + de 40 Interprétation: obésité morbide ou massive ")
elif imc>35:
    print("IMC : 35 à 40 Interprétation: obésité sévère ")
elif imc>30:
    print("IMC : 30 à 35 Interprétation: obésité modérée ")
elif imc>25:
    print("IMC : 25 à 30 Interprétation: Surpoids ")
elif imc>18.5:
    print("IMC : 18.5 à 25 Interprétation: corpulence normale ")
elif imc>16.5:
    print("IMC : 16.5 à 18.5 Interprétation: Maigreur ")
else :
    print("IMC : - de 16.5 Interprétation: Famine ")
