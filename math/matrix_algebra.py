# Matrix Algebra

import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

alpha = 6

dimensions = {
    'A': A.shape,
    'B': B.shape,
    'C': C.shape,
    'D': D.shape,
    'u': u.shape,
    'v': v.shape
}

print(dimensions)
print(np.add(u,v))
print(np.add(u,-v))
print(np.multiply(alpha, u))
print(np.dot(u,v))
print(np.linalg.norm(u))
# print(np.add(A,C))
print(np.add(A,-np.transpose(C)))
print(np.add(np.transpose(C),np.multiply(3,D)))
print(np.dot(B,A))
# print(np.dot(B,np.transpose(A)))
# print(np.dot(B,C))
print(np.dot(C,B))
print(np.power(B,4))
print(np.dot(A,np.transpose(A)))
print(np.dot(np.transpose(D),D))
