from preambleparser import preamble
from factorparser import factorparse
from readfiles import readfile
import numpy as np

import tensorly as tl
from tensorly.decomposition import Parafac2
from tensorly.decomposition import parafac
from preambleparser import stv


a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")

def getallmatrices(a):
    #cardinality = preamble(a)
    vectors = factorparse(a)
    matricenetwork = []
    card = a[2]
    card = stv(card, " ")
    high = int(max(card)) 
    #print(high)
    t1 = (16,1)
    t2 = (high ,1)
    t1 = (16,16)
    #print(t1 > t2)

    for i in range(len(vectors)):
        tensor = np.array(vectors[i])
     #   print(tensor.shape)
        if(tensor.shape > t2):
            weights, matrices = parafac(tensor, rank=3)
            matricenetwork.append(matrices)
        else:
            matricenetwork.append([])
    #print(matricenetwork)
    return matricenetwork


