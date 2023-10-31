L=[20,100,2,9,-9,180,57,5,9,100,25,9]
print("L est une liste , L= ",L)
num=int(input("Donnez un nombre que vous voullez supprimer dans cette liste L : "))
[L.remove(i) for i in L if num==i]
print("Alors L après la suppression est la suivantes : ",L)
