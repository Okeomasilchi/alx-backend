#!/usr/bin/env python3

"""
index_range that takes two integer arguments
page and page_size.
"""


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
