"""
Docstring for 7-advanced_numpy.6-stacking
vertically 
horizontally  
vstack() row wise 
hstack() column wise
"""

import numpy as np  
arr1  = np.array ([1,3,4])
arr2   =  np.array ([4,5,6])
print (np.vstack((arr1,arr2))) #vertically stack
print (np.hstack((arr1,arr2)))#horizontally stack