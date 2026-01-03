"""
fancy index --> selecting multiple element ones 
"""

import numpy as np  
arr  = np.array([1,2,3,4,5]) 
print(arr[[0,3]])#ints use for 1d 

arr1  = np.array([[2,3,4,5],
                  [3,4,5,6]]) 
print(arr1[1 ,[1,3]]) #its user for multidimensinal