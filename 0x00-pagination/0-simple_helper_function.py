#!/usr/bin/env python3


""" Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """
    function index_range that takes 2 args and returns a tuple
    Args:
        page (int): The page number.
        page_size (int): The number of items per page.
    Returns:
        tuple: The start and end index of the range
        of items to be displayed on the page.
    """
    end = page * page_size
    start = end - page_size
    return start, end
