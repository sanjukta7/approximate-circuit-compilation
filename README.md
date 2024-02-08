# approximate-circuit-compilation

UAI-2014 Files structure: \\ 
<Preamble> 
<Function-Table> 

MARKOV
3
2 2 3
2
2 0 1
2 1 2
2
 0.436 0.564

4
 0.128 0.872
 0.920 0.080

6
 0.210 0.333 0.457
 0.811 0.000 0.189

for the preamble:
1: name or the type of the PGM in the file 
2: Number of variables in the network 
3: cardinality of the variables in the network, this is a vector of size int(line(2)) 
4: Number of factors or cliques in the network 
5: onwards, until all the factors are described - starts with a number of variables in the factor, and the the index of the variables in the factor 


for the function-table: all the function table (each corressponding to a factor follows the same structure) 
1: the number of parameters in the table 
2: onwards, the parameters in either pairs or triplet figures. 

