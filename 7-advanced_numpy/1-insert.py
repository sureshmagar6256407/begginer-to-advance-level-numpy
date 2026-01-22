"""
Docstring for 7-advanced_numpy.1-insert
np.insert(array,index,value,axis=None)
array  - original array  
index  - position where the new value is inserted
value  - the value to be inserted
axis - axis along which to insert the new value (default is None, which flattens the array)
"""
import numpy as np  
arr = np.array ([10,30,29,40,29])
print(arr)
new_arr  = np.insert(arr ,2,[49,20],axis=None)
print(new_arr)
