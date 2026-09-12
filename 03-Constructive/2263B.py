"""
Day 133: Codeforces 2263B - Matrix Construction / Swap Logic
Topic: Constructive Algorithms / Implementation
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`.
3. Check if `k` is within the valid range `[n, 2 * n - 1]`. If not, it's impossible, so print `-1`.
4. Initialize an $n \times n$ matrix with sequential values.
5. Calculate the required `num_swaps` based on `k` and perform the targeted element swaps.
6. Print the modified matrix row by row.

Complexity Analysis:
- Time: O(N^2) per test case - for initializing and printing the n x n matrix.
- Space: O(N^2) - to store the grid.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())

        if k < n or k > 2 * n - 1:
            print(-1)
            continue

        s_arr = [[(i * n) + j for j in range(1, n + 1)] for i in range(n)]

        num_swaps = (2 * n - 1) - k

        for j in range(1, num_swaps + 1):
            s_arr[0][j], s_arr[j][j] = s_arr[j][j], s_arr[0][j]

        for row in s_arr:
            print(*(row))

if __name__ == "__main__":
    solve()