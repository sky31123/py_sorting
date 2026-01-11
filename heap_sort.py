# heap_sort.py
from typing import List

def heapify_down(arr: List[int], length: int, index: int) -> None:
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < length and arr[left] > arr[largest]:
        largest = left
    if right < length and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify_down(arr, length, largest)

def heap_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range((n-1)//2, -1, -1):
        heapify_down(arr, n, i)
    #Max Heap, keep moving a[0] to i from end to convert into sorted array
    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr, i, 0)

def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 6, 3, 5, 5, 3, 2, 1, 3, 5, 6, 7, 8, 3]
    heap_sort(arr)
    print(arr)

if __name__ == '__main__':
    SystemExit(main())