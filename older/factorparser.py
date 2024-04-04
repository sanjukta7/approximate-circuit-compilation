from preambleparser import preamble
from preambleparser import stv
import numpy as np


from readfiles import readfile

a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")


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

def factorparse(a):
    anew = []
    cardinality = preamble(a)
    start = len(cardinality) + 5
    end = len(a)
    for i in range(start, end):
        aupd = stvstr(a[i], "\n")
        anew.append(aupd)
    afinal = []
    for i in range(len(anew)):
        temp = anew[i][0]
        if (i%2 == 0):
            afinal.append(temp)
        else:
            temp = stvfloat(temp, " ")
            afinal.append(temp)
    vectors = []
    for i in range(len(afinal)):
        if i%2 == 0:
            halfi = int(i/2)
            lenvalact = cardinality[halfi]
        else:
            anp = np.array(afinal[i])
            anp = anp.reshape(lenvalact)
            vectors.append(anp)
    return vectors 

