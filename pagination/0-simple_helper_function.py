#!/usr/bin/env python3
"""a function named index_range that takes two
integer arguments page and page_size"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index
                         for the items corresponding to the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
