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
    print(partitions)

else:
    files=None

filename=comm.scatter(files,root=0)

for i in range(size):
    if i==rank:
        print("I am rank %s\n"%rank)
        print('show files I got')
        print(filename)

