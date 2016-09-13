import os
from os.path import join
from glob import glob
from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size

if rank==0:
    template=join(os.getcwd(),'t*.txt')
    files=glob(template)
    partitions=[[] for i in range(size)]
    for i,file in enumerate(files):
        partitions[i%size].append(file)
    print('partitions=%s\n'%partitions)
    for i in range(len(partitions)):
        comm.isend(partitions[i],dest=i,tag=i)

filelist=comm.recv(source=0,tag=rank)
print('I am rank {} of size {}'.format(rank,size))
print(filelist)
for file in filelist:
    with open(file,'w') as f:
        f.write("rank {} wrote this file".format(rank))
print('finish rank %s'%rank)

