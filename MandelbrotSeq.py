import numpy as np 
import matplotlib.pyplot as plt 
import time
def mandelbrot(x,y,maxit):
    c=x+y*1j#complex exporession
    z=0+0j#complex expression
    it=0
    while   abs(z)<2 and it<maxit:
        z=z**2+c
        it+=1
    return it

#main
x1,x2=-2.0,1.0
y1,y2=-1.0,1.0
w,h=150,100
maxit=1025

C=np.zeros([h,w],dtype=int)

dx=(x2-x1)/w
dy=(y2-y1)/h
start=time.time()
for i in range(h):
    y=y1+i*dy
    for j in range(w):
        x=x1+j*dx
        C[i,j]=mandelbrot(x,y,maxit)
plt.imshow(C, aspect="equal")
plt.spectral()
end=time.time()
elapsed_time=end-start
print("time= %s" % elapsed_time)
plt.show()