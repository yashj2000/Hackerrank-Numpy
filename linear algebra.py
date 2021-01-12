import numpy as np 



a=np.ones((2,3))
b=np.full((3,2),2)
print(np.matmul(a,b)) #matrix multi reqs col1=row2 and row1 = col2


#find determinant
c=np.identity(3)
print(np.linalg.det(c))



#inverse mat
