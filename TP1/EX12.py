grade=input("Donnez votre type de grade (A-B-C-D-E) : ")
while(grade!='A' and grade!='B' and grade!='C' and grade!='D' and grade!='E'):
    grade=input("Donnez votre type de grade (A-B-C-D-E) : ")

heure=int(input("Donnez le nombre d'heure de votre travaille : "))
match grade:
    case 'A':
        salaire=200*heure+1000*(heure//20)
        print(f"Grade A : {grade} \n-Tarif horaire : 200dh \n-Prime : 1000dh pour chaque 20 heures de travail ")
        print(f"Votre salaire = {salaire} dh")
    case 'B':
        salaire=150*heure+800*(heure//20)
        print(f"Grade B : {grade} \n-Tarif horaire : 150dh \n-Prime :800dh pour chaque 20 heures de travail ")
        print(f"Votre salaire = {salaire} dh")
    case 'C':
        salaire=120*heure+500*(heure//15)
        print(f"Grade C : {grade} \n-Tarif horaire : 120dh \n-Prime : 500 pour chaque 15 heures de travail ")
        print(f"Votre salaire = {salaire} dh")
    case 'D':
        salaire=100*heure+350*(heure//15)
        print(f"Grade D : {grade} \n-Tarif horaire : 100dh \n-Prime : 350dh pour chaque 15 heures de travail ")
        print(f"Votre salaire = {salaire} dh")
    case 'E':
        salaire=80*heure+100*(heure//10)
        print(f"Grade E : {grade} \n-Tarif horaire : 80dh \n-Prime : 100dh pour chaque 10 heures de travail ")
        print(f"Votre salaire = {salaire} dh")