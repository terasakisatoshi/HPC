from mpi4py import MPI
import numpy as np 
sendbuf=[]
root =0
comm=MPI.COMM_WORLD
if comm.rank==0:
    m=np.random.randn(comm.size,comm.size)
    print(m)
    sendbuf=m
v=comm.scatter(sendbuf,root)
print("I got this array")
print(v)