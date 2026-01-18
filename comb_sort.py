# comb_sort.py
from typing import List

def next_gap(current: int) -> int:
    return max(1, int( current / 1.3) )

def comb_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = next_gap(gap)
        if gap == 1:
            print()
        swapped = False
        for i in range(0, n-gap): #pythonic way. when i reaches n-gap end will be n, so range 0 to n - gap.
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swapped = True
    return arr

def main():
    #arr = [4, 3, 6, 7, 8, 9, 4, 5, 6, 3, 5, 5, 3, 2, 1, 3, 5, 6, 7, 8, 3]
    arr = [2, 0, 3, 4, 5, 6, 1] #used comb_sort_tester to find an example which needs at least one more pass after gap is 1 to be sorted.
    arr = [2, 1, 3, 4, 3, 2, 3, 5]
    print(comb_sort(arr))
    print(8//1.3)

if __name__=='__main__':
    main()