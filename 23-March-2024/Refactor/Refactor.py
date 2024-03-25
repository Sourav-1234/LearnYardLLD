from typing import List, Callable
from NumberStrategy import NumberStrategy

def sum_by_test(nums: List[int], selector: Callable[[int], bool]) -> int:
    return sum(num for num in nums if selector(num))

def sum_by_test_refactored(nums: List[int], selector: Callable[[int], bool]) -> int:
    return sum(num for num in nums if selector(num))

if __name__ == "__main__":
    object = NumberStrategy.NumberStrategy
    print(sum_by_test_refactored([1, 2, 3, 4, 5], object.pass_all))
    print(sum_by_test_refactored([1, 2, 3, 4, 5], object.is_even))
    print(sum_by_test_refactored([1, 2, 3, 4, 5],object.is_odd))

    print(sum_by_test_refactored([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 4, 15], object.is_prime))

    print(sum_by_test_refactored([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 4, 15], object.is_fibonacci))