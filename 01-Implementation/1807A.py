"""
Day 89: Plus or Minus (Codeforces 1807A)
Topic: Implementation
Logic:
1. We are given three integers a, b, and c. It is guaranteed that either a + b = c or a - b = c.
2. We check the condition (a + b == c). If it is true, the operator is '+', so we print "+".
3. Otherwise, by elimination, the operator must be '-', so we print "-".

Complexity Analysis:
- Time: O(1) per test case - Basic constant time arithmetic check.
- Space: O(1) - Uses primitive integers with no extra memory allocation.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())

        # Check if addition satisfies the equation
        if a + b == c:
            print("+")
        else:
            print("-")

if __name__ == "__main__":
    solve()