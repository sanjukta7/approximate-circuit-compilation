D = [[1,1,2], [1,0,4], [0,0,4], [0,1,5]]
import numpy as np 

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


print(d3)
print(len(d3))