"""
slicin-arr[start : stop:step]
"""

import numpy as np  
arr = np.array([10,30,40,50,20,50]) 
print(arr[0:3])
print (arr[:3])  
print(arr[ :: 2])
print(arr[ ::-1])


arr1  = np.array ( [[2,3,4,5] , 
                    [6,7,8,9]]) #this is use for multdimensioal accesing
print(arr1[1 ,1 : ])