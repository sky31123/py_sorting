from itertools import permutations

def next_gap(current: int) -> int:
    return max(1, int(current / 1.3))

def comb_sort_trace(arr):
    """Return True if we ever reach gap==1 at top of loop while array is unsorted."""
    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        # Check condition: gap==1 at top AND array unsorted
        if gap == 1 and any(arr[i] > arr[i+1] for i in range(n-1)):
            return True  # Found a counterexample

        gap = next_gap(gap)
        swapped = False

        for i in range(0, n-gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swapped = True

    return False  # Never saw gap==1 with unsorted array

def search_size_7():
    base = [0,1,2,3,4,5,6]
    for perm in permutations(base):
        arr = list(perm)
        if comb_sort_trace(arr.copy()):
            print("FOUND COUNTEREXAMPLE:", arr)
            return
    print("No counterexample exists for size 7.")

search_size_7()
