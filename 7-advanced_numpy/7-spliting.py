"""
Docstring for 7-advanced_numpy.7-spliting
np.split(array, indices_or_sections, axis=0)
np.hsplit(array, indices_or_sections)
np.vsplit(array, indices_or_sections)
"""

import numpy as np 
arr  = np.array ([10,30,49,50,60,90])
print (np.split(arr, 2))