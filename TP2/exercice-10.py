L1=[35,1,3,6,78,35,88,55]
L2=[12,24,35,24,88,120,155]
L3=[]
for i in L1:
    for j in L2:
        if i==j:
            if i not in L3:
                L3.append(i)
print(L3)
