X=[]
f=open("EllipticIntegralKk_writefiles.txt","r")
for line in f:
    X.append(line.replace("\n",""))
f.close()
print(X)
