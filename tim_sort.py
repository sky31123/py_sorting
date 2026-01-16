# tim_sort.py
from typing import List

MIN_RUN = 8

def calculate_runsize(n: int) -> int:
    r = 0
    while n > MIN_RUN:
        if n % 2 != 0:
            r = n % 2
        n = n//2
    return n + r

def merge(arr: List[int], l1: int, l2: int, r2: int) -> None:
    a1 = arr[l1:l2]
    a2 = arr[l2:r2]
    i, j, k = 0, 0, l1
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
    return

def insertion_sort(arr: List[int], start: int, end: int) -> None:
    for i in range(start+1, end):
        key = arr[i]
        j = i-1
        while arr[j] > key and j>=start:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return


def get_next_run(arr, start):
    n = len(arr)
    end = start + 1
    if end == n:
        return end
    #ascending
    if arr[end] >= arr[end-1]:
        while end < n and arr[end-1] <= arr[end]:
            end += 1
    #descending
    else:
        while end < n and arr[end-1] > arr[end]:
            end += 1
        arr[start:end] = list(reversed(arr[start:end]))
    return end


def tim_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    runs = []
    min_run = calculate_runsize(n)
    i = 0
    while i < n:
        end = get_next_run(arr, i)
        run_len = end - i
        if run_len < min_run:
            end = min(i+min_run, n)
            insertion_sort(arr, i, end)
        runs.append((i, end))
        i = end

        while len(runs) >= 3:
            A = runs[-3][1] - runs[-3][0]
            B = runs[-2][1] - runs[-2][0]
            C = runs[-1][1] - runs[-1][0]

            #Invariant 1 A must be > B + C, if not merge A and B
            if A <= B + C or B < C:
                #merge smaller of A and C with neighbor
                if A < C:
                    merge(arr, runs[-3][0], runs[-2][0], runs[-2][1])
                    runs[-3] = (runs[-3][0], runs[-2][1])
                    runs.pop(-2)
                else:
                    merge(arr, runs[-2][0], runs[-1][0], runs[-1][1])
                    runs[-2] = (runs[-2][0], runs[-1][1])
                    runs.pop()
            else:
                break

    while len(runs) > 1:
        merge(arr, runs[0][0], runs[1][0], runs[1][1])
        runs[0] = (runs[0][0], runs[1][1])
        runs.pop(1)

    return arr

def main():
    arr = [4, 3, 6, 7, 8, 9, 4, 5, 0, 6, 3, 5, 5, 3, 2, 1, 3, 0, 5, 6, 7, 8, 3, 4, 3, 11, 3, 5, 5, 3, 2, 1, 3, 0, 5, 6, 7, 8, 3]
    arr = tim_sort(arr)
    print(arr)

if __name__ == '__main__':
    SystemError(main())