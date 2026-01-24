import numpy as np  

arr1  = np.array ([[1,2,3] , [
    4,5,6
] ])
arr2 = np.array([1,2])
res  = arr2.reshape (2,1) 
print(res)
result = arr1 + res 
print(result)