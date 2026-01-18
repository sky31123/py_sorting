# bubble_sort.py

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1): #largest element gets bubbled up after every iteration of outer loop
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
        print(arr[len(arr)-1])
    return arr

def main():
    arr = [4,3,6,7,8,9,4,10,5,6,3,5,5,3,2,1,3,5,6,7,8,3]
    print(bubble_sort(arr))

if __name__ == '__main__':
    main()