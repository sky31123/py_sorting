# quick_sort.py
from typing import List

def partition(arr: List[int], left: int, right: int) -> int:
    pivot = right - 1
    j = left
    for i in range(left, right - 1):
        if arr[i] <= arr[pivot]:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j

def quick_sort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)

def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 6, 3, 5, 5, 3, 2, 1, 3, 5, 6, 7, 8, 3]
    quick_sort(arr, 0, len(arr))
    print(arr)

if __name__=='__main__':
    main()