from mpi4py import MPI
comm =MPI.COMM_WORLD
print "Hello,World! My rank is: " +str(comm.rank)
