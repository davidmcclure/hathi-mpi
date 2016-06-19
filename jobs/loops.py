

from mpi4py import MPI

from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume


def loops():

    """
    Generate and processs the paths in parallel - break of N paths, send to
    worker, break off another N paths, etc.
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    # TODO


if __name__ == '__main__':
    loops()
