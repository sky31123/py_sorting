# merge_sort.py
from math import ceil, floor
from typing import List


def merge(arr: List[int], low: int, mid: int, high: int) -> None:
    a1 = [arr[i] for i in range(low, mid+1)]
    a2 = [arr[i] for i in range(mid+1, high+1)]
    k = low
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            arr[k] = a1[i]
            i += 1
        else:
            arr[k] = a2[j]
            j += 1
        k += 1
    while i < len(a1):
        arr[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        arr[k] = a2[j]
        j += 1
        k += 1

def merge_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        mid = low + int((high-low)/2)
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 6, 3, 5, 5, 3, 2, 1, 3, 5, 6, 7, 8, 3]
    merge_sort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == '__main__':
    main()