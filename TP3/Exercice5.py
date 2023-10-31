def conversion_distances(km,m,cm):
    m=km*1000+m+cm*0.01
    return m
print("La distance 5km 410m 10cm d'ou : distance en metre : ",conversion_distances(5,410,10))
