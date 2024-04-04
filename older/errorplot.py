from cperror import finderror 
from readfiles import readfile 
import numpy as np
import matplotlib.pyplot as plt


a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")
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

