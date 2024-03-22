# all imports for the CP decomposition and basic structuring. 
import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

import cirkit 

# setup the weight matrices: 
A = np.array([[0,1,3],[4,5,63],[6,7,8],[2,3,5]])
B = np.array([[1,1,2], [1,0,4], [0,0,4], [0,1,5]])
# - more weight matrices yet to be initialised here. 

# weight matrices after the decomposition here: 
weightsa, factorsa = parafac(A, rank=2)
weightsb, factorsb = parafac(B, rank=2)


for factors in factorsa: 
    print(factors)
print("this is B")
for factors in factorsb: 
    print(factors)


# setup the input matrices here: 
Ia = np.array([0,0,1,0])
Ib = np.array([0,1,0,0])
# - more input matrices are yet to be initialised here. 


