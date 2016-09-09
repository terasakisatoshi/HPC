from mpi4py import MPI 
import numpy as np 

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
name=MPI.Get_processor_name()

sendbuf=np.zeros(10,dtype='i')+rank
print('I am rank {} I have sendbuf as {}'.format(rank,sendbuf))
recvbuf=None

if rank==0:
    recvbuf=np.empty([size,10],dtype='i')

comm.Gather(sendbuf,recvbuf,root=0)

if rank==0:
    print("I am maseter i.e. rank={} I gathered recvbuf as\n {}".format(rank,recvbuf))
    for i in range(size):
        assert np.allclose(recvbuf[i,:],i)