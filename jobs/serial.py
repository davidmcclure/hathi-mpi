

import atexit

from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume


def serial():

    """
    Loop through volmes one-by-one.
    """

    corpus = Corpus.from_env()

    v = 0
    t = 0

    @atexit.register
    def log():
        print(v, t)

    for path in corpus.paths('.bz2'):

        try:

            vol = Volume.from_bz2_path(path)
            t += vol.token_count()
            v += 1

        except Exception as e:
            print(e)


if __name__ == '__main__':
    serial()
