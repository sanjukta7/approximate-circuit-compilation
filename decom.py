import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

#tensor_random = np.random.random((3,4))

tensor_random = np.array([[0,1,3],
                          [4,5,63],
                          [6,7,8], 
                            [2,3,5]])
weights, factors = parafac(tensor_random, rank=1)

print(tensor_random)
print(weights)
for factor in factors: 
    print(factor)
    print(len(factor))