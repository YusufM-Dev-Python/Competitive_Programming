"""
Day 139: Codeforces 2266B - Math / Implementation
Topic: Greedy / Math
Logic:
1. Read the number of test cases `t`.
2. For each testcase, read integers `a`, `b`, and `c`.
3. Compute and print the maximum possible absolute difference according to the problem constraints (`max(abs(a - b), abs(a + c - b))`).

Complexity Analysis:
- Time: O(1) per testcase - basic arithmetic operations.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())

        print(max(abs(a - b), abs(a + c - b)))

if __name__ == '__main__':
    solve()