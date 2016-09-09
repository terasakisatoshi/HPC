from mpi4py import MPI 
import numpy as np 
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
name=MPI.Get_processor_name()

if rank==0:
    data=np.arange(10,dtype='i')
    print('Hello I am rank {} of size={} on {}'.format(rank,size,name))
    comm.Send([data,MPI.INT],dest=1,tag=44)
elif rank==1:
    data1=np.empty(10,dtype='i')
    comm.Recv([data1,MPI.INT],source=0,tag=44)
    print("Hello I am rank {} of size={} on {}".format(rank,size,name))
    print("I received data ={}".format(data1))
