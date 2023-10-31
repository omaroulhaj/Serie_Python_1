
def somme(n,m):
    s=0
    if(n<m):
        for i in range(n,m+1):
            s+=i
    return s
n=somme(10,15)
print(n)