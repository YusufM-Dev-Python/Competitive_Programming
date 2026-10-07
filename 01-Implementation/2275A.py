"""
Day 152: Codeforces 2275A - Implementation / Geometry
Topic: Implementation / Basic Math
Logic:
1. Read the number of test cases `t`.
2. For each test case, read the circle's center coordinates `x0`, `y0`, and its radius `r`.
3. Compute the required output point (e.g., the rightmost point on the circle at `x0 + r`, keeping `y0` constant) and print the result.

Complexity Analysis:
- Time: O(1) per test case - constant time arithmetic calculation.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        x0, y0, r = map(int, input().split())

        print(x0 + r, y0)

if __name__ == "__main__":
    solve()