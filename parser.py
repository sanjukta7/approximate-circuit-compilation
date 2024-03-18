import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

# Create a random 3-order tensor
tensor = np.random.random((3, 4, 2))

# Perform CP decomposition
weights, factors = parafac(tensor, rank=3)

print(tensor)
# Print results
print("Weights:", weights)
print("Factor matrices:")
for factor in factors:
    print(factor)
    print(len(factor))