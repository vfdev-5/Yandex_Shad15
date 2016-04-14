__author__ = 'vfdev'

import numpy as np

n = 3

matrix = np.ones((2*n, 2*n))*10


# first move
matrix[0, 0] = 10



def check(m):
    if m.any() == np.NAN:
        print "Has NAN"
        m = np.nan_to_num(m)
    eye = np.eye(m.shape[0])
    d = np.linalg.det(m - eye)
    return d


print matrix

print check(matrix)