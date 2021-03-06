# https://www.geeksforgeeks.org/python-program-for-binary-search/
def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index > len(array)-1:
        return None
    if array[index] == item:
        return index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    array.sort()
    start = 0
    end = len(array) - 1
    while start <= end:
        midpoint = (start + end) // 2
        if array[midpoint] == item:
            return midpoint
        elif array[midpoint] < item:
            start = midpoint + 1
        elif array[midpoint] > item:
            end = midpoint - 1

    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    array.sort()
    midpoint = (left + right) // 2
    if array[midpoint] == item:
        return midpoint
    elif left > right:
        return None

    if array[midpoint] < item:
        left = midpoint + 1
        return binary_search_recursive(array, item, left, right)
    if array[midpoint] > item:
        right = midpoint - 1
        return binary_search_recursive(array, item, left, right)
