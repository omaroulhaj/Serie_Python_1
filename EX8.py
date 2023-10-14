note=[]
coeficient=[]
somme=0
c=0
for i in range(0,4):
    note.append(float(input(f"Note {i+1} = ")))
    coeficient.append(float(input(f"Coeficient de cette note  = ")))
    somme+=note[i]*coeficient[i]
    c+=coeficient[i]
moyenne=somme/c
print(f"Moyenne de ces 4 notes : {moyenne}")
if moyenne>10:
    print("Semestre Validé")
elif moyenne>=7:
    print("Ratrrapage")
else :
    print("Semestre non validé")