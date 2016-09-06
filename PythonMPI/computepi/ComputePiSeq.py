import math
import time
#compute \pi using formula shown below:
#\pi=\int_{0}^{1}\frac{4}{1+x^2}dx \sim =\frac{1}{n}\sum_{i=0}^{n-1}\frac{4}{1+(\frac{i+0.5}{n})^2}
#
def compute_pi(num_step):
    h=1.0/num_step
    s=0.0
    for i in range(num_step):
        x=h*(i+0.5)
        s+=4.0/(1.0+x**2)
    return s*h

def main():
    n=int(1.0e8)
    start=time.time()
    pi=compute_pi(n)
    diff=abs(pi-math.pi)
    print("pi is approximately %.16f,diff=compute_pi-math.pi is %.16f" % (pi,diff))
    elapsed_time=time.time()-start
    print("elapsed_time=%f" % elapsed_time )

if __name__ == '__main__':
    main()