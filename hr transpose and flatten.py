import numpy as np 

n=int(input())
arr = np.array([input().split() for i in range(n)],int)

print(np.transpose(arr))
print(arr.flatten())