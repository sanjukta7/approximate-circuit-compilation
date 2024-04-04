from cpdecomposition import getallmatrices
from factorparser import factorparse
from readfiles import readfile
from readfiles import readfolder
import numpy as np
import random

a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")
def util1(factor, listval):
    numvars = len(listval)
    theta = 0 
    for i in range(numvars):
        theta = factor[listval[i]]
        factor = theta
    return theta

def adjustmax(cardinal):
    newcardinal = []
    for i in range(len(cardinal)):
        newcardinal.append(cardinal[i] - 1)
    return newcardinal


def finderror(a):
    matrices = getallmatrices(a)
    factors = factorparse(a)
    # this gives all the factors of the network a and all the matrices of those factors 
    totalfactors = len(factors)
    #print(totalfactors)
    error = []
    for i in range(totalfactors):
        testfactor = np.array(factors[i])
        #print(testfactor.shape)
        if (list(testfactor.shape)[1] == 1): 
            cardinal = np.array(list(testfactor.shape)[0])
            #print(cardinal)
            testerror = 0 
            samplesize = 5 
            for s in range(samplesize):
                val = random.randint(0,cardinal)
                #print(val)
                testoutcome = 0 
                testerror = testerror + testoutcome
            error.append(testerror/samplesize)
        else:
            cardinal = list(testfactor.shape)
            cardinal = adjustmax(cardinal)
            #print(cardinal)
            cardinal0 = [0] * len(cardinal)
            testerror = 0 
            samplesize = 5 
            for s in range(samplesize):
                values = [random.randint(min_value, max_value) for min_value, max_value in zip(cardinal0, cardinal)]
                testvalue = util1(testfactor,values)
                testmatrice = np.array(matrices[i])
                #print(testmatrice.shape)
                nummatrices = list(testmatrice.shape)[0]
                #print(nummatrices)
                rank = list(testmatrice[0].shape)[-1]
                #print(rank)
                productmatrice = [1] * rank
                for p in range(nummatrices):
                    #print(testmatrice[p].shape)
                    newmatrice = testmatrice[p]
                    varvalue = values[p]
                    #print(varvalue)
                    #print(newmatrice[varvalue])
                    productmatrice = productmatrice * newmatrice[varvalue]
                #print(productmatrice)
                sample_error = 0 
                for r in range(rank):
                    #print(productmatrice[r])
                    sample_error = sample_error + productmatrice[r]
            testerror = testerror + abs(sample_error - testvalue)
            if (testvalue != 0):
                testerror = testerror/testvalue *100 
        testerror = testerror / samplesize
        print(testerror) 
        error.append(testerror)
    return error 

a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")
error = finderror(a)
print(error)