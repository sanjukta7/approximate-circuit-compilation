import numpy as np

filename = "/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/segmentation_16.uai"
with open(filename, 'r') as f: 
    lines = f.readlines()
    vs, cs = int(lines[1]), int(lines[3])
    cardinality = lines[2]
    cardinality = cardinality.split()
    lines = lines[4:]
    lines = [line for line in lines if line != "\n"]

def factor(vl,cpt,cardinality):
    dimension = []
    for i in range(len(vl)):
        #print(vl[i])
        varname = int(vl[i])
        dimension.append(int(cardinality[varname]))

    cpt = np.array(cpt)
    dimension = np.array(dimension)
    factor = cpt.reshape(dimension)
    return factor


varlist = lines[:cs]
cptlist = lines[cs+1::2]
print(len(varlist))
print(len(cptlist))
factors = []

for i in range(cs):
    cpt = list(map(float, cptlist[i].split()))
    vl = list(map(int, varlist[i].split()))[1:]
    factors.append(factor(vl,cpt,cardinality))
    print(cpt)
    print(factor(vl,cpt,cardinality))

    

print(factors[2])
print(factors[2].shape)