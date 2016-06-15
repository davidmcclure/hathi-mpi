

import atexit

from hathi_mpi.corpus import Corpus


if __name__ == '__main__':

    """
    Loop through volmes one-by-one.
    """

    corpus = Corpus.from_env()

    v = 0
    t = 0

    @atexit.register
    def log():
        print(v, t)

    for vol in corpus.volumes():
        t += vol.token_count()
        v += 1
