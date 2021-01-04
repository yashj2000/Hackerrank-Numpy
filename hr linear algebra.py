import numpy as np
n=int(input())
a=np.array([input().split() for i in range(n)],float)
b=np.linalg.det(a)
print(round(b,2))