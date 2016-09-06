from mpi4py import MPI 
comm=MPI.COMM_WORLD
rank=comm.rank
name=MPI.Get_processor_name()
data1={}
data2={}
if rank==0:
    data1={"a":1,"b":2,"c":3}
    data2={"d":4,"e":5,"f":6}
else:
    data=None
print("Hello I'm %s and my rank is %d"%(name,rank))
receive1=comm.bcast(data1,root=0)
receive2=comm.bcast(data2,root=0)
print(receive1)
print(receive2)
