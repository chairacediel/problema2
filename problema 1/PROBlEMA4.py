import random as random
from time import time

c=0
x=[]
inicio= time()

#for i in range(4000):
    #x.append(random.randint(1,2000))

for i in range(800):
    x.append(random.randint(1601,2000))
for i in range(800):
    x.append(random.randint(1201,1600))
for i in range(800):
    x.append(random.randint(801,1200))
for i in range(800):
    x.append(random.randint(401,800))
for i in range(800):
    x.append(random.randint(1,400))

def burbuja_optimus(x):
    n = len(x)
  
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            if x[j] > x[j+1] :
                x[j], x[j+1] = x[j+1], x[j]
                intercambio = True
        if intercambio == False:
            break

burbuja_optimus(x)
tiempo = time() - inicio
print(x)
print("Tiempo de ejecucion",tiempo)