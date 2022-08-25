from time import time
import random as random


inicio= time()
c=0
x=[]
for i in range(10000):
    x.append(random.randint(0,1000))
    if x[i]%2==0:
        c=c+1

if c>0:
    print("Porcentaje es igual a: ",(c/10000)*100,"%")
else:
    print("No se generaron numeros pares")

tiempo = time() - inicio
print("Tiempo de ejecucion",tiempo)

