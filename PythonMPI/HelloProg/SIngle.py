import numpy as np 

size=100
m=np.array([np.ones(4)*i for i in range(size)])
print(m)

for i in range(size):
    m[i]=m[i]*m[i]
print(m)