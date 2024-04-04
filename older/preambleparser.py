import numpy as np
from readfiles import readfile

a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")


def stv(vec, sep):
    vec = vec.split(sep)
    temp = len(vec)
    vecupd = []
    for i in range(temp-1):
        vecupd.append(int(vec[i]))
    return vecupd

def preamble(a): 
    card = a[2]
    card = stv(card, " ")
    cardtemp = []
    cardinality = []
    num_factors = int(a[3])
    for i in range(4, 4+num_factors):
        #print(a[i])
        temp = stv(a[i]," ")
        cardtemp.append(temp)
    for i in range(len(cardtemp)):
        temp = cardtemp[i]
        cardinality.append([])
        for j in range(1,len(temp)):
            tempcard = card[temp[j]]
            cardinality[i].append(tempcard)
            #print(len(temp))
            if (len(temp) == 2):
                cardinality[i].append(1)
    return (cardinality)

