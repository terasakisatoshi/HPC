from mpi4py import MPI
import math
import time

def compute_pi(n,start=0,step=1):
    h=1.0/n
    s=0.0
    for i in range(start,n,step):
        x=h*(i+0.5)
        s+=4.0/(1.0+x**2)
    return s*h

def main():
    comm =MPI.COMM_WORLD
    nprocs=comm.Get_size()
    myrank=comm.Get_rank()

    if myrank==0:
        start=time.time()
        n=int(1.0e7)
    else:
        start=None
        n=None

    n=comm.bcast(n,root=0)
    mympi=compute_pi(n,myrank,nprocs)

    pi=comm.reduce(mympi,op=MPI.SUM,root=0)

    if myrank ==0:
        diff=abs(pi-math.pi)
        print ("pi is approximately %.16f, error is %.16f" % (pi,diff))
        elapsed_time=time.time()-start
        print("elapsed_time=%f" % elapsed_time )
if __name__ == '__main__':
    main()
