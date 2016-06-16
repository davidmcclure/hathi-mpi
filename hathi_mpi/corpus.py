

import scandir
import os
import json

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


    def paths(self, ext):

        """
        Generate .bz2 asset paths.

        Args:
            ext (str)

        Yields: str
        """

        for root, dirs, files in scandir.walk(self.path):
            for name in files:
                if os.path.splitext(name)[1] == ext:
                    yield os.path.join(root, name)


    def bz2_volumes(self):

        """
        Generate .bz2 volume instances.

        Yields: Volume
        """

        for path in self.paths('.bz2'):
            yield Volume.from_bz2_path(path)


    def json_volumes(self):

        """
        Generate .json volume instances.

        Yields: Volume
        """

        for path in self.paths('.json'):
            yield Volume.from_json_path(path)
