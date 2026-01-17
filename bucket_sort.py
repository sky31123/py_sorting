# bucket_sort.py
from typing import List

def insertion_sort(arr: List[int]):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def bucket_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    buckets = [[] for _ in range(n)]
    #No fixed bucketing algorithm
    for i in range(n):
        buckets[min(arr[i]//n, n-1)].append(arr[i])
    i = 0
    for bucket in buckets:
        b = len(bucket)
        if b <= 0:
            continue
        insertion_sort(bucket)
        arr[i:i+b] = bucket
        i += b

def main():
    arr = [4, 5, 10, 36, 27, 543, 1032, 3, 54, 21]
    bucket_sort(arr)
    print(arr)

if __name__ == '__main__':
    main()