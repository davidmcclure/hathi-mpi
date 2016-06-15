

import atexit

from multiprocessing import Pool

from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume


if __name__ == '__main__':

    """
    Loop through volmes one-by-one.
    """

    corpus = Corpus.from_env()

    def worker(path):
        vol = Volume.from_path(path)
        return vol.token_count()

    v = 0
    t = 0

    @atexit.register
    def log():
        print(v, t)

    with Pool() as pool:

        jobs = pool.imap_unordered(worker, corpus.paths())

        for count in jobs:
            t += count
            v += 1
