import sympy
#Find the nth Prime number
n=25
th=0
i=0
while th<n:
    i=i+1
    if sympy.isprime(i):
        th=th+1
print("The "+str(n)+" th prime number is "+str(i))


