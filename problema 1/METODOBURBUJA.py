import random as random

c=0
x=[]

for i in range(1000):
    x.append(random.randint(0,1000))
    if x[i]%2==0:
        c=c+1

def burbuja_optimus(x):
    n = len(x)
  
    for i in range(0.1000):
        intercambio = False
 
        for j in range(n-1-i):
            if x[j] > x[j+1] :
                x[j], x[j+1] = x[j+1], x[j]
                intercambio = True
        if intercambio == False:
            break

burbuja_optimus(x)

print(x)