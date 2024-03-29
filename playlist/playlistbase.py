"""File to modify the playlists."""

from layx.logger import (
    Logger
)

from layx.stringutils import remove_duplicates


# Setup logger
logger = Logger('PlaylistBase')


class SongMetadataBase:
    """
    Base class to store song metadata.
    """

    def __init__(self):
        self.title = ''
        self.search_querry = ''
        self.URL = ''
        self.better_search_kw = [
                                # ' audio',
                                # ' lyrics',
                                # ' full'
                                ]

    def _add_better_search_words(self):
        """
        Add the keywords in better_search_kw list to get a better result.
        """
        for kw in self.better_search_kw:
            self.search_querry += kw

    def _remove_duplicates(self):
        """
        Remove duplicate words from the searchquerry.
        """
        self.search_querry = remove_duplicates(self.search_querry)

    def content(self):
        """
        Show the content of the class
        """
        return "{}:{}:{}".format(
                                self.title,
                                self.URL,
                                self.search_querry
                            )


class PlaylistBase:
    """
        Base class for all the playlist that implements some common functionalitites
        such as fixing the start-end markers
    """
    def __init__(self, pl_start=-1, pl_end=-1):
        self.pl_start = pl_start
        self.pl_end = pl_end
        self.list_content_tuple = []

    def _is_valid(self, s, e):
        if s and e:
            return len(range(s, e)) > 0

    def strip_to_start_end(self):
        """
            Strip the tuple to positions passed by the user.
            First check if start and end are in increasing range.
            Then truncate the markers based on the size of the list.
        """
        # Update the length of the playlist
        if not self.pl_start or self.pl_start < 1:
            self.pl_start = 1
        if not self.pl_end or self.pl_end < 1:
            self.pl_end = len(self.list_content_tuple)

        # reset marker to make sure it's in the order given by start/end
        start = min(self.pl_start, self.pl_end)
        end = max(self.pl_start, self.pl_end)
        step = 1 if (self.pl_start <= self.pl_end) else -1
        if self._is_valid(start, end):
            self.list_content_tuple = self.list_content_tuple[start-1 : end]
            if step == -1:
                self.list_content_tuple = self.list_content_tuple[::-1]