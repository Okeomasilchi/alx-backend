#!/usr/bin/env python3
"""model that holds the class Server and index_range funtion"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start
    index and end index for pagination.

    Args:
        page (int): The current page number
          (1-indexed).
        page_size (int): The number of items
          per page.

    Returns:
        tuple: A tuple containing the start
        index and end index.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """class initilization"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns page data after paginating"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > (len(data) / end) and end < (len(data) % page_size):
            return []
        else:
            return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns hyper page data after paginating"""
        data = self.get_page(page, page_size)
        total_page = math.ceil(len(self.__dataset) / page_size)
        nxt = page + 1 if page < total_page else None
        prev = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": nxt,
            "prev_page": prev,
            "total_pages": total_page
        }
