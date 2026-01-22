"""
Docstring for 7-advanced_numpy.7-spliting
np.split(array, indices_or_sections, axis=0)
np.hsplit(array, indices_or_sections)
np.vsplit(array, indices_or_sections)
"""

import numpy as np 
# arr  = np.array ([10,30,49,50,60,90])
# print (np.split(arr, 2))
# print (np.hsplit(arr,2))


arr_2d  = np.array([[1,2,3,11] , 
                    [4,5,6,12] , 
                    [7,8,9,10]])
print (np.hsplit(arr_2d,2))
print (np.vsplit(arr_2d,3))
print (np.split(arr_2d,3 ,axis= 0))
print (np.split(arr_2d , 2 ,axis =1 ))