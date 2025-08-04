"""
A module containing an implementation of a binary search algorithm.
"""
import random

def binary_search(binary_list: list, target: int) -> int | None:
    """
    Implementation of binary search in python
    Time complexity is
    :param binary_list: List of integers to search
    :param target: Target value
    :return: The index at which the target was found, else none
    """
    first = 0
    last = len(binary_list) - 1

    while first <= last:
        middle = (first + last) // 2 # Make sure we do floor division

        if binary_list[middle] == target:
            return middle
        elif binary_list[middle] < target:
            first = middle + 1
        else:
            last = middle -1


    return None


def verification(index: int):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found in list")


def main():
    numbers = [i for i in range(0, 100)]
    target = random.randint(0, len(numbers) - 1)
    print(f"The target is {target}")

    verification(binary_search(numbers, target))
    verification(binary_search(numbers, target + 100))


if __name__ == '__main__':
    main()