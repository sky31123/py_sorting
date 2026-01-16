MIN_RUN = 32

# ---------------------------------------------------------
# Correct Timsort version (ACCUMULATES lost bits)
# ---------------------------------------------------------
def calcMinRun_timsort(n):
    r = 0
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r

# ---------------------------------------------------------
# Your version (OVERWRITES r each iteration)
# ---------------------------------------------------------
def calcMinRun_yours(n):
    r = 0
    while n >= MIN_RUN:
        if n%2 != 0:
            r = n % 2      # overwrite, not accumulate
        n = n // 2
    return n + r

# ---------------------------------------------------------
# Compare both for a range of N
# ---------------------------------------------------------
def compare_all(start=1, end=3000):
    print(f"Comparing outputs for N = {start} to {end}")
    print("Showing only mismatches:\n")

    mismatches = 0

    for n in range(start, end + 1):
        a = calcMinRun_timsort(n)
        b = calcMinRun_yours(n)

        if a != b:
            mismatches += 1
            print(f"N={n:3d}   Timsort={a:3d}   Yours={b:3d}")

    print(f"\nTotal mismatches: {mismatches}")

# ---------------------------------------------------------
# Run comparison
# ---------------------------------------------------------
compare_all()
