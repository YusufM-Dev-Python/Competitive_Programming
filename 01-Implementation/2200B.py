"""
Day 154: Codeforces 2200B - Implementation / Array Property
Topic: Implementation / Sorting Check
Logic:
1. Use fast I/O (`sys.stdin.read`) to read all tokens efficiently.
2. For each test case, read length `n` and array `a`.
3. Check if the array is already non-decreasing using `all()`.
4. If it is already sorted, output `n`. Otherwise, output `1`.

Complexity Analysis:
- Time: O(N) per test case - a single linear pass to check sorted order.
- Space: O(N) - to store the input array and output buffer.
"""

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = [int(data[idx + i]) for i in range(n)]
        idx += n

        # Check if the array is already non-decreasing
        is_sorted = all(a[i] <= a[i + 1] for i in range(n - 1))

        if is_sorted:
            out.append(str(n))
        else:
            out.append("1")

    print("\n".join(out))

if __name__ == "__main__":
    solve()