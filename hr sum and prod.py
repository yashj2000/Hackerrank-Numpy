import numpy as np 
a,b=map(int,input().split())
arr=np.array([input().split() for i in range(a)],int)
print(np.prod(np.sum(arr,axis=0),axis=0))
