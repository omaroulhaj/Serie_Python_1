second=int(input("Saisir  les secondes pour convertir aux format (hh:mm:ss) : "))
heur=second//3600
minute=(second-heur*3600)//60
s=second-heur*3600-minute*60

print(f"{second} au format {heur}h {minute} min {s} sec")
