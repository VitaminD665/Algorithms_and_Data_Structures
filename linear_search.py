"""
Module containing an implementation of linear search
"""
import random

def linear_search(List: list, target: int) -> int | None:
    """
    Linear Search Example
    :param List: Entered list
    :param target: Target value index
    :return: The index position of the target if found, else None
    """
    for i in range(len(List)):
        if List[i] == target:
            return i

    return None

def verification(index: int) -> None:
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found in list")


def main():

    numbers = [i for i in range(100)]
    target = random.randint(0, 100)
    print(f"The target is {target}")

    verification(linear_search(numbers, target))
    verification(linear_search(numbers, target + 100))


if __name__ == '__main__':
    main()