"""
Day 144: Codeforces 2229A - Meeting Point / Brute Force
Topic: Brute Force / Implementation / Math
Logic:
1. Fast I/O is used to read all tokens at once.
2. For each test case, read `n` and the array `a` representing positions.
3. Find the minimum and maximum values in the array to bound the search space.
4. Iterate through every possible meeting position `p` between `min_val` and `max_val`, calculating the maximum distance from any point to `p`.
5. Track the minimum of these maximum distances (`ans`) and print the results separated by newlines.

Complexity Analysis:
- Time: O(T * N * (max - min)) per test case - optimal when the range of values is small.
- Space: O(N) - to store input data and output tokens.
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
        a = [int(x) for x in data[idx : idx + n]]
        idx += n

        min_val = min(a)
        max_val = max(a)

        ans = float("inf")
        # Try every possible meeting position P between min and max initial positions
        for p in range(min_val, max_val + 1):
            max_dist = max(abs(x - p) for x in a)
            ans = min(ans, max_dist)

        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    solve()