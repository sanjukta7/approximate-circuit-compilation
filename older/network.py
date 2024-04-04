
filename = "/Users/sanjukta/Documents/GitHub/approximate-circuit-compilation/benchmarksUAI/examples/csp_13.uai"
with open(filename, 'r') as f: 
    lines = f.readlines()
    vs, cs = int(lines[1]), int(lines[3])
    lines = lines[4:]
    lines = [line for line in lines if line != "\n"]

print(lines[910])
print(lines[905:915])
print(lines[912])
temp = int(lines[912])
print(lines[913: 913 + temp])


print(len(lines), 3*cs)
varlist = lines[:cs]
cptlist = lines[cs+1::2]
factors = []
