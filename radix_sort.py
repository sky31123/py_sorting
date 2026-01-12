# radix_sort.py
from typing import List


def radix_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    div = 1
    while True:
        all_done = True
        count = [0] * 10
        for i in range(0, n):
            if arr[i] / div > 1:
                all_done = False
            count[(arr[i]//div)%10] += 1
        if all_done:
            break
        for i in range(1, 10):
            count[i] += count[i-1]
        ans = [0] * n
        for i in range(n-1, -1, -1):
            ans[count[(arr[i]//div)%10]-1] = arr[i]
            count[(arr[i]//div)%10] -= 1
        div *= 10
        arr = ans
    return arr

def main():
    arr = [300, 456, 21, 7896, 345612, 90, 873, 6647, 21334]
    arr = radix_sort(arr)
    print(arr)

if __name__ == '__main__':
    SystemError(main())