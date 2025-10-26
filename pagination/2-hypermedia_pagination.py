#!/usr/bin/env python3
"""
Pagination module.

This module provides a Server class that paginates data
from a CSV file using page and page_size parameters and
returns hypermedia pagination metadata.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
                         for the items corresponding to the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache dataset from CSV file.

        Returns:
            List[List]: The dataset loaded from the CSV file,
                        with the header row removed.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page from the dataset.

        Args:
            page (int, optional): The current page number (1-indexed).
                                  Defaults to 1.
            page_size (int, optional): Number of items per page.
                                       Defaults to 10.

        Returns:
            List[List]: The list of rows corresponding to the requested page.
                        Returns an empty list if the page is out of range.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieve a page of the dataset with pagination metadata.

        Args:
            page (int, optional): The current page number (1-indexed).
                                  Defaults to 1.
            page_size (int, optional): Number of items per page.
                                       Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing the following keys:
                - page_size: number of items in the current page
                - page: current page number
                - data: the dataset page
                - next_page: next page number, or None if no next page
                - prev_page: previous page number, or None if no previous page
                - total_pages: total number of pages in the dataset
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if page_size else 0

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        hyper_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hyper_data
