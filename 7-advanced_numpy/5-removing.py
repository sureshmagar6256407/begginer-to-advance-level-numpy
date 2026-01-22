"""
Docstring for 7-advanced_numpy.5-removing
np.delete(array, index,axis = none)
array - original array
index - position of the element to be deleted
axis - axis along which to delete the element (default is None, which flattens the array)
"""
import numpy as np   
arr = np.array ([10,30,40,39])
print (arr)
new_arr = np.delete(arr,1, axis=None)
print (new_arr)

arr_2d = np.array ([[2,2,4] ,
                    [5,6,7]])
print (arr_2d)
new = np.delete(arr_2d,1,axis=1)
print (new)