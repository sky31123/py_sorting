# insertion_sort.py
from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    return arr


def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 6, 3, 5, 5, 3, 2, 1, 3, 5, 6, 7, 8, 3]
    print(insertion_sort(arr))

if __name__=='__main__':
    main()