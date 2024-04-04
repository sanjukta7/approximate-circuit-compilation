
def error(a,fac):
    matrices = getallmatrices(a)
    factors = factorparse(a)

    testfactor = np.array(factors[fac]) 
    print(testfactor.shape)
    cardvars = list(testfactor.shape)



cardinality = preamble(a)
start = len(cardinality) + 5
end = len(a)

print(start)
print(end)
print(a[start])
print(a[start + 1])

error = 0 
matrices = getallmatrices(a)
factors = factorparse(a)
# use factors and matrices now on. 
i = 187
testfactor = np.array(factors[i])
print("-----------")
print(testfactor.shape)
#print(testfactor)
#this will a 16 X 16 testfactor
(x,y) = testfactor.shape
# x = 16,  y = 16 
valx = random.randint(1,x) - 1
valy = random.randint(1,y) - 1
#insantiated random values. lets not for now. 
valx = 5
valy = 3
testval = testfactor[valx][valy]
print(testval)
print("this is the test value to wokrk with")
testmatrice = np.array(matrices[i])
print(testmatrice.shape)
#  (n, vali, r) is the shape of the test matrice
val = 0
tempmatricex = testmatrice[0][valx]
tempmatricey = testmatrice[1][valy]
print(tempmatricex)
print(tempmatricey)
for r in range(len(tempmatricey)):
    val = val + tempmatricex[r]*tempmatricey[r]
error = abs(testval - val)
print(val)
print(testval)
print(error)
print(error/testval *100)