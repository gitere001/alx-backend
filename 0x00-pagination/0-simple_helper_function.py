#!/usr/bin/env python3
"""A module containing index_range"""


def index_range(page, page_size):
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
