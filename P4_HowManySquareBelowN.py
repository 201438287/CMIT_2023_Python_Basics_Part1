import math
N=1000
count=0
for i in range(N):
    sqrt=math.pow(i,1/2)
    # int rounds sqrt to neares integer
    if sqrt==int(sqrt):
        count=count+1
print("There are "+str(count)+" square numebers below "+str(N))

