L=[20,100,2,9,-9,180,57,200,2,9,-9,20,-9,60,71,-9,-9,-9,20]
L.sort()
print(L)
i=0
while len(L)!=i+1:
    if L[i]==L[i+1]:
        del L[i]
        print(L)
        continue
    i+=1
print(L)