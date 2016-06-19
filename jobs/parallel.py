

import atexit

from multiprocessing import Pool

from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume


def count_tokens(path):

    """
    Count tokens in a volume.

    Args:
        path (str)
    """

    try:

        vol = Volume.from_bz2_path(path)
        return vol.token_count()

    except Exception as e:
        print(e)


def parallel():

    """
    Parallelize across N cores.
    """

    corpus = Corpus.from_env()

    v = 0
    t = 0

    @atexit.register
    def log():
        print(v, t)

    with Pool() as pool:

        jobs = pool.imap_unordered(
            count_tokens,
            corpus.paths('.bz2'),
        )

        for count in jobs:
            if count: t += count
            v += 1


if __name__ == '__main__':
    parallel()
