import numpy as np
n,m=map(int,input().split())
matrix=np.array([input().split() for i in range(n)],int)
print(np.max(np.min(matrix,axis=1)))