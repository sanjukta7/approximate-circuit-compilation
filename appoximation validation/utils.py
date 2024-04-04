import numpy as np
import os
import tensorly as tl
from tensorly.decomposition import parafac



directory = "/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/"

def readfile(directory):
    with open(os.path.join(directory)) as f:
        a = f.readlines()
    return a


def foldertonetwork(directory):
    file_names = os.listdir(directory)
    allnetworks = []
    print(file_names)
    for file in file_names:
        filename = str(file)
        metadirectory = directory + filename
        allnetworks.append(readfile(metadirectory))
    return allnetworks 

def factor(vl,cpt,cardinality):
    dimension = []
    for i in range(len(vl)):
        varname = int(vl[i])
        dimension.append(int(cardinality[varname]))

    cpt = np.array(cpt)
    dimension = np.array(dimension)
    factor = cpt.reshape(dimension)
    return factor

def networktofactor(network): 
    lines = network
    vs, cs = int(lines[1]), int(lines[3])
    cardinality = lines[2]
    cardinality = cardinality.split()
    lines = lines[4:]
    lines = [line for line in lines if line != "\n"]
    varlist = lines[:cs]
    cptlist = lines[cs+1::2]
    factors = []
    for i in range(cs):
        cpt = list(map(float, cptlist[i].split()))
        vl = list(map(int, varlist[i].split()))[1:]
        factors.append(factor(vl,cpt,cardinality))
    return factors
    
def factorcpdecomposition(factor, rank):
    weights = []
    decomposedfactors = []
    error = []
    if len(np.array(factor).shape) != 1:
        (weights, decomposedfactors), error = parafac(factor, rank, return_errors=True)
        return weights, decomposedfactors, error
    else:
        return weights, decomposedfactors, error
    
def getnormerrorr(error):
    avgerror = 0 
    for eacherror in error:
        avgerror += eacherror
    if len(error) == 0:
        return avgerror
    else:  
        avgerror = avgerror/len(error)
        return avgerror

#def errorplot(error):
