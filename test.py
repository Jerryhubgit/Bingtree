import numpy as np


twoDList = [[0,1,2], 
            [3,-1,5], 
            [6,7,8]]
# array = np.array(twoDList, dtype = bool)
# thisList = array.tolist()
# print(f'thisList: {thisList}, type: {type(thisList)}')

# print(type(array))
# print(type(twoDList))

thisTuple = (1,2,3,4)

array = np.array([thisTuple], dtype= float)
print(array.dtype)