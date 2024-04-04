from cpdecomposition import getallmatrices
from factorparser import factorparse
from readfiles import readfile
from readfiles import readfolder
import numpy as np
import random
import matplotlib.pyplot as plt
from cperror import finderror 
from readfiles import readfile 

a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/segmentation_16.uai")
def ploterror(data):
    plt.figure(figsize=(8, 10))
    # Plot box plot
    plt.boxplot(data, patch_artist=True)

    plt.xlabel('Data')
    plt.ylabel('Values')
    plt.title('Box Plot')
    plt.grid(True)
    plt.show()

error = finderror(a)
ploterror(error)