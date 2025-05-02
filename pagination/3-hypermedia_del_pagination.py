#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math  # noqa: F401
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Retrieves a page of data from the indexed dataset starting from a
        given index.
        Ensures deletion resilience pagination, meaning it works correctly
        even if some entries are deleted.
        Args:
            index (int, optional): The starting index for data retrieval.
            Defaults to 0.
            page_size (int, optional): The number of items to
            retrieve per page.
            Defaults to 10.

        Returns:
            Dict: A dictionary with the following keys:
                - index (int): The starting index of the current page.
                - next_index (int): The index for the next page of data.
                - page_size (int): The number of items in the current page.
                - data (List[List]): The list of data items for the
                current page.
        """
        # Retrieve the indexed dataset from the Server class
        indexed_data = self.indexed_dataset()

        # Ensure the index is an integer and in the valid range
        assert isinstance(index, int)
        assert 0 <= index < len(self.dataset())

        data = []
        next_index = index
        collected = 0

        # Collect items until the desired page size is reached
        while collected < page_size:
            # Check if the current next_index exists in the indexed dataset
            if next_index in indexed_data:
                # Append the data at the current next_index to the data list
                data.append(indexed_data[next_index])
                # Increment the collected counter
                collected += 1
            # Move to the next index
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
