

import numpy as np

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

    # Make path segments.

    if rank == 0:

        corpus = Corpus.from_env()

        paths = list(corpus.paths('.bz2'))

        segments = np.array_split(paths, size)

    else:
        segments = None

    # Count tokens in segment.

    segment = comm.scatter(segments, root=0)

    count = 0

    for path in segment:

        try:

            vol = Volume.from_bz2_path(path)
            count += vol.token_count()

        except Exception as e:
            print(e)

    # Merge segment sub-totals.

    counts = comm.gather(count, root=0)

    if rank == 0:
        print(sum(counts))


if __name__ == '__main__':
    scatter()
