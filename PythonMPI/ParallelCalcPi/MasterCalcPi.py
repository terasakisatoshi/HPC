
from mpi4py import MPI
import numpy
import sys

N = 1000000

print ("--------------- PI ---------------")
print ("N: %d" % N)

comm = MPI.COMM_WORLD.Spawn(sys.executable,
                           args=['SlaveCalcPi.py'],
                           maxprocs=15)
# Broadcast a message from one process to all other processes in a group
comm.bcast(N, root=MPI.ROOT)

PI = 0.0
# Reduce
PI = comm.reduce(None, PI, op=None, root=MPI.ROOT)

print "PI =", PI

comm.Disconnect()

print ("----------------------------------")