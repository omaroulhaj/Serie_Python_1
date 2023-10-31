def conversion_temps(h,m,s):
    return h*3600+m*60+s
def temps_ecoule(h1,m1,s1,h2,m2,s2):
    s2=conversion_temps(h1,m1,s1)
    s1=conversion_temps(h2,m2,s2)
    if s1-s2<0 :
        return s2-s1
    else :
        return s1-s2

print("Temps 1 : 4h20m30s , Temps 2 : 6h24m40s le temps ecoulé est en seconde s = ",temps_ecoule(6,24,40,6,24,40))