# counting_sort.py
import math
from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    #max element in array for count array size
    max_element = max(arr)
    count = (max_element+1) * [0]
    #increase count in count array based on arr
    for i in range(0,n):
        count[arr[i]] += 1
    #prefix sum
    #you can recreate the array with just count array but it won't be stable and if it were object instead
    for i in range(1, len(count)):
        count[i] += count[i-1]
    arr1 = n * [-1]
    for i in range(n-1, -1, -1):
        arr1[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return arr1

def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 0, 6, 3, 5, 5, 3, 2, 1, 3, 0, 5, 6, 7, 8, 3]
    arr = counting_sort(arr)
    print(arr)

if __name__ == '__main__':
    main()