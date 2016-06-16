

from mpi4py import MPI

from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume


def scatter():

    """
    Walk all paths, scatter to workers, rather sub-sums.
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:

        corpus = Corpus.from_env()

        paths = list(corpus.paths('.bz2'))

        segments = np.array_split(paths, size)

    else:
        segments = None

    segment = comm.scatter(segments, root=0)

    count = 0

    for path in segment:
        vol = Volume.from_bz2_path(path)
        count += vol.token_count()

    # TODO: gather


if __name__ == '__main__':
    scatter()
