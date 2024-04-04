from utils import readfile
from utils import foldertonetwork
from utils import factor
from utils import networktofactor
from utils import factorcpdecomposition
from utils import getnormerrorr

import numpy as np
import os
import tensorly as tl
from tensorly.decomposition import parafac 
import matplotlib.pyplot as plt


directory = "/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/"
networks = foldertonetwork(directory)
print(len(networks))
mainerror = []
for network in networks:
    networkerror = []
    factors = networktofactor(network)
    for factor in factors:
        tempfactor = np.array(factor)
        weight, decomposedfactor, normerror = factorcpdecomposition(tempfactor, rank=2)
        err = getnormerrorr(normerror)
        networkerror.append(err)
    mainerror.append(networkerror)
    print(networkerror)
print(mainerror)

plt.figure(figsize=(8, 10))
# Plot box plot
plt.boxplot(mainerror, patch_artist=True)

plt.xlabel('Networks')
plt.ylabel('Absolute error')
plt.title('The Frobenius norm of Markov Networks')
plt.grid(True)
plt.savefig('example1.png')
plt.show()