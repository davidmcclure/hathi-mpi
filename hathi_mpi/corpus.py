

import scandir
import os

from hathi_mpi.volume import Volume
from hathi_mpi import config


class Corpus:


    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined corpus root.

        Returns: cls
        """

        return cls(config['corpus_dir'])


    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)


    def paths(self):

        """
        Generate asset paths.

        Yields: str
        """

        for root, dirs, files in scandir.walk(self.path):
            for name in files:
                yield os.path.join(root, name)


    def volumes(self):

        """
        Generate volume instances.

        Yields: Volume
        """

        for path in self.paths():
            yield Volume.from_path(path)
