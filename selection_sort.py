# selection_sort.py
import math
from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 6, 3, 5, 5, 3, 2, 1, 3, 5, 6, 7, 8, 3]
    print(selection_sort(arr))

if __name__ == '__main__':
    main()