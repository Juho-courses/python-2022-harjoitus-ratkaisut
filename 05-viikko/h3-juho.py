from typing import List


def filter_values(numbers: List[int], divider: int = 2) -> List[int]:
    return [n for n in numbers if n % divider == 0]


print(filter_values([1, 2, 3, 4, 5, 6]))
print(filter_values([1, 2, 3, 4, 5, 6], 3))
