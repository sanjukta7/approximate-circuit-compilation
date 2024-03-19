import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

#tensor_random = np.random.random((3,4))

tensor_random = np.array([[0,1,3],
                          [4,5,63],
                          [6,7,8], 
                            [2,3,5]])
weights, factors = parafac(tensor_random, rank=1)

#print(tensor_random)
#print(weights)
#for factor in factors: 
 #   print(factor)
  #  print(len(factor))

D = [[1,1,2], [1,0,4], [0,0,4], [0,1,5]]

d_np = np.array(D)
print(d_np)

d3 = []
f = 4

for i in range(f):
    d3.append([])
    for j in range(f):
        d3[i].append([])
        for k in range(f):
            d3[i][j].append([])
            if (i == j == k):
                d3[i][j][k]  = D[i][2]
            else:
                d3[i][j][k] = 0
d3 = np.array(d3)
weights, factors = parafac(d3, rank=2)

print(d3)
print(weights)
for factor in factors: 
    print(factor)
    print(len(factor))