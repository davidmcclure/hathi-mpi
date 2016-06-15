

import atexit

from hathi_mpi.corpus import Corpus


if __name__ == '__main__':

    """
    Loop through volmes one-by-one.
    """

    corpus = Corpus.from_env()

    i = 0
    c = 0

    @atexit.register
    def log():
        print(i, c)

    for vol in corpus.volumes():
        c += vol.token_count()
        i += 1
