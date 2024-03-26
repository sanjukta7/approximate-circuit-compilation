import numpy as np


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

    num_factors = int(a[3])

    for i in range(4, 4+num_factors):
        print(a[i])
        temp = stv(a[i]," ")
        cardtemp.append(temp)

    #print(preamble(a))
    #num_vars, num_funcs, card = preamble(a)

    #print(type(card))
    cardinality = []
    for i in range(len(cardtemp)):
        temp = cardtemp[i]
        #print(temp)
        #print(type(temp))
        cardinality.append([])
        #print(cardinality[i])
        for j in range(1,len(temp)):
            #this is already an integer 
            #print(temp[j])
            tempcard = card[temp[j]]
            cardinality[i].append(tempcard)
            #print(tempcard)
        #print(cardinality)
    return (cardinality)

#print(preamble(a))

