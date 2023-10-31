def conversion_distances(km,m,cm):
    m=km*1000+m+cm*0.01
    return m
def conversion_temps(h,m,s):
    return h*3600+m*60+s
print("La distance 14km et 500m,10cm le temps ecoulé temps 2h50min35s La vitesse de V1 = ",conversion_distances(14,500,10)/conversion_temps(2,50,35),"m/s")