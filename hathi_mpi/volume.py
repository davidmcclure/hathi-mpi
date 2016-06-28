

import json
import bz2


class Volume:

    @classmethod
    def from_bz2_path(cls, path):

        """
        Inflate a .bz2 volume and make an instance.

        Args:
            path (str)

        Returns: cls
        """

        with bz2.open(path, 'rt') as fh:
            return cls(json.loads(fh.read()))

    @classmethod
    def from_json_path(cls, path):

        """
        Inflate a .json volume and make an instance.

        Args:
            path (str)

        Returns: cls
        """

        with open(path, 'r') as fh:
            return cls(json.loads(fh.read()))

    def __init__(self, data):

        """
        Read the compressed volume archive.

        Args:
            data (dict)
        """

        self.data = data

    def id(self):

        """
        Get the HTRC id.

        Returns: str
        """

        return self.data['id']

    def token_count(self):

        """
        Get the total token count on all pages.

        Returns: int
        """

        return sum([
            page['tokenCount']
            for page in self.data['features']['pages']
        ])
