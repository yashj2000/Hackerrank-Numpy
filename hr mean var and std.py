import numpy as np
n,m=map(int,input().split())
matrix=np.array([input().split() for i in range(n)],int)
print(np.mean(matrix,axis=1))
print(np.var(matrix,axis=0))
std=np.std(matrix)
print(round(std,11))