#!/usr/bin/env python3

"""
    Pagination project: task 0
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Takes page number and page size, and returns a tuple of size two
        containing a start index and an end index corresponding to the range of
        indexes to return in a list for those particular pagination parameters.
        => Page numbers are 1-indexed.
    """
    return ((page - 1) * page_size, page * page_size)
