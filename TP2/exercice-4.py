L=[1,-30,0,-2,500,4,2,100]
# M=list(L) # M=L[:] n'est pas M=L
M=[]
[M.append(i) for i in L if i<0 ]
[M.append(i) for i in L if i>0 ]
print(M)
