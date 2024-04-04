import os
import re


def readfile(directory):
    with open(os.path.join(directory)) as f:
        a = f.readlines()
    return a

def readfolder(filename):
    directory = "/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/"
    directory = directory + filename
    return readfile(directory)


def readfolder(directory):
    file_names = os.listdir(directory)
    allnets = []
    for file in file_names:
        filename = str(file)
        metadirectory = directory + filename
        allnets.append(readfile(metadirectory))

    return allnets 