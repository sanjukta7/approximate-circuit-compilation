from preambleparser import preamble
from preambleparser import stv
import numpy as np


from readfiles import readfile

a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")
cardinality = preamble(a)

start = len(cardinality) + 5
end = len(a)

print(start)
print(end)
print(a[start])
print(a[start + 1])

def stvstr(vec, sep):
    vec = vec.split(sep)
    temp = len(vec)
    vecupd = []
    for i in range(temp-1):
        vecupd.append(vec[i])
    return vecupd

def stvfloat(vec, sep):
    vec = vec.split(sep)
    temp = len(vec)
    vecupd = []
    for i in range(temp-1):
        vecupd.append(float(vec[i]))
    return vecupd

anew = []

for i in range(start, end):
    aupd = stvstr(a[i], "\n")
    anew.append(aupd)


afinal = []
for i in range(len(anew)):
    temp = anew[i][0]
    if (i%2 == 0):
        print(temp)
        afinal.append(temp)
    else:
        temp = stvfloat(temp, " ")
        print(temp)
        print(len(temp))
        afinal.append(temp)

vectors = []
for i in range(len(afinal)):
    if i%2 == 0:
        #print(int(afinal[i]))
        lenval = int(afinal[i])
        halfi = int(i/2)
        lenvalact = cardinality[halfi]
        #print(lenvalact)
    else:
        anp = np.array(afinal[i])
        anp = anp.reshape(lenvalact)
        #print(anp)
        vectors.append(anp)


print(vectors)
print(vectors[60])
print(vectors[194])
