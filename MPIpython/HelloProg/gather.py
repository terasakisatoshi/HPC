from mpi4py import MPI
import numpy as np 
sendbuf=[]
root =0
comm=MPI.COMM_WORLD
name=MPI.Get_processor_name()
size=MPI.COMM_WORLD.Get_size()
rank=MPI.COMM_WORLD.Get_rank()
if comm.rank==0:
    m=np.array([np.ones(4)*i for i in range(size)])
    print(m)
    sendbuf=m
    print("sending message completed")

v=comm.scatter(sendbuf,root)
print("My rank is %d and name is %s I got this array %s"% (rank,name,v))
v=v*v
recvbuf=comm.gather(v,root)
if comm.rank==0:
    print("the result is....")
    print np.array(recvbuf)