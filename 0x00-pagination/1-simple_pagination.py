#!/usr/bin/python3

"""
    Pagination project: task 1
"""


import csv
import math
from typing import List, Tuple


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ initializes a Server instance """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Takes two integer arguments as pagination parameters:
            @page: with default value 1
            @page_size: with default value 10
            Returns the appropriate page of the dataset from the CSV file
            If the input arguments are out of range for the dataset,
            an empty list should be returned.
        """
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0)
        assert(page_size > 0)

        pages = []
        data = self.dataset()
        indexes = index_range(page, page_size)

        if indexes[0] > len(self.__dataset) - 1 or \
           indexes[1] > len(self.__dataset) - 1:
            return []

        for i in range(indexes[0], indexes[1]):
            pages.append(data[i])
        return pages


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Takes page number and page size, and returns a tuple of size two
        containing a start index and an end index corresponding to the range of
        indexes to return in a list for those particular pagination parameters.
        => Page numbers are 1-indexed.
    """
    return ((page - 1) * page_size, page * page_size)
