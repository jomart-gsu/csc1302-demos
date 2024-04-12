# NumPy challenges from the slides
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])


# 1
arr.transpose()
arr.T  # also works if your hands hurt from typing too much

# 2
np.delete(arr, 0, axis=1)
arr[:,1:]  # also works -- this is the fun slicing we get to do with 2D arrays

# 3
np.sort(arr)  # could use axis=0 argument to sort column-wise

# 4
np.ravel(arr)
arr.flatten()  # also works

# 5
# there are probably many ways to do this, but this is the one I found
np.concatenate((arr, arr.mean(axis=1, keepdims=True)), axis=1)

# note that arr.mean(axis=1) produces the mean of every row in arr!
