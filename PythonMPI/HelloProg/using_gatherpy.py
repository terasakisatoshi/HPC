from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

def dlg(data):
    print "rank",rank,"has data",data
    print "now we modify data by adding plus 1 into data"
    data+=1
    print "return data"
    return data

if rank==0:
    #if we change range size more than 'size'
    #this script stops.
    data=[(x+1)**x for x in range(size)]
    print "We will be scattering ",data
else:
    data=None

data=comm.scatter(data,root=0)
data1=dlg(data)
newData=comm.gather(data1,root=0)
if rank==0:
    print "master collected:", newData
