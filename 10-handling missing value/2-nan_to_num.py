# np.nan_to_num(array,nan=value)-0

import numpy as np  
arr = np.array([1,np.nan ,2,3, np.nan,5])
cleaned_arr  =np.nan_to_num(arr,nan =100)
print(cleaned_arr)