from preambleparser import preamble
from readfiles import readfile
import os

a = readfile("/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/objectdetection_320.uai")
cardinality = preamble(a)

for i in range(len(cardinality)):
    print(cardinality[i])

