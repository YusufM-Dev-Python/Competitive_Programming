"""
Day 155: Codeforces 2271A - Parity Implementation & Case Analysis
Topic: Implementation / Math / Parity Conditions
Logic:
1. Read the number of test cases `t`.
2. For each test case, read inputs `a` and `b`.
3. Check the parity of the sum `(a + b)`:
   - If even, check if `b <= a`. If true, print `a`, otherwise print `-1`.
   - If odd, check if `b <= a + 1`. If true, print `a + 1`, otherwise print `-1`.

Complexity Analysis:
- Time: O(1) per test case - constant time arithmetic and condition checks.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())

        if (a + b) % 2 == 0:
            print(a if b <= a else -1)
        else:
            print(a + 1 if b <= a + 1 else -1)

if __name__ == "__main__":
    solve()