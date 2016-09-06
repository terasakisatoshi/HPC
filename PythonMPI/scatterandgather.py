from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size

if rank==0:
    data=[(x+1)**x for x in range(size)]
    print( 'will be scattering %s'%data)
else:
    data=None

data=comm.scatter(data,root=0)

print('rank %s has data %s'%(rank,data))

data+=1
newData=comm.gather(data,root=1)

if rank==1:
    print('rank %d collected%s'%(rank,newData))