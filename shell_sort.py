# shell_sort.py
from typing import List


def shell_sort(arr: List[int]):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i-gap
            while j >= 0 and arr[j] > key:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = key
        gap = gap // 2

def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 0, 6, 3, 5, 5, 3, 2, 1, 3, 0, 5, 6, 7, 8, 3]
    shell_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()