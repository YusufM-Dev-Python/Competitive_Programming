"""
Day 157: Codeforces 2276A - Implementation / Boundary Analysis
Topic: Implementation / Greedy / Math
Logic:
1. Read the number of test cases `t`.
2. For each test case, read inputs `a` and `b`.
3. Check the base constraint: if `b >= a`, it's impossible to satisfy the condition, so output `-1`.
4. Otherwise, return the minimum of `b` and `a - b`.

Complexity Analysis:
- Time: O(1) per test case - constant time conditional checks.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())

        if b >= a:
            print(-1)
        else:
            print(min(b, a - b))
    
if __name__ == "__main__":
    solve()