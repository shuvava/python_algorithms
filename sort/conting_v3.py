# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2026 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Counting sort
Complexity: O(n+k);
  where n length of an element array and k range of elements
"""


def sort(arr: list[int]) -> list[int]:
    """
    Sorts an array of integers using the counting sort algorithm.
    """
    if len(arr) < 2:
        return arr  # trivial case
    max_val = max(arr)

    # Create frequency table
    freq = [0] * (max_val + 1)
    for num in arr: freq[num] += 1
    for num in range(1, len(freq)): freq[num] += freq[num - 1]

    # Create places table
    sorted_arr = [0] * len(arr)
    for num in arr:
        sorted_arr[freq[num] - 1] = num
        freq[num] -= 1
    return sorted_arr


if __name__ == '__main__':
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
    ]
    for arr, expected in test_cases:
        assert sort(arr) == expected, f"Failed for {arr}"
