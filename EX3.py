distance=float(input("Saisir ici la distance (KM) : "))
temps=float(input("Saisir ici le temps (Min) : "))
temps*=60 #pour convertir le temps du minute au seconds
distance*=1000 #pour convertir la distance du KM au Metre
vitesse=distance/temps
print(f"La vitesse est : {vitesse} m/s")
