import os
import re


def readfile(directory):
    with open(os.path.join(directory)) as f:
        a = f.readlines()
    return a
