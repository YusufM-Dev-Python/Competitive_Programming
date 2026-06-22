"""
Day 84 (Bonus): Odd One Out (Codeforces 1915A)
Topic: Implementation / Brute Force
Logic:
1. We are given three digits (a, b, c) where two of them are identical and one is different.
2. We check all three possible pairs of equality:
   - If a == b, then 'c' must be the unique number.
   - If b == c, then 'a' must be the unique number.
   - If a == c, then 'b' must be the unique number.
3. The matching condition executes and prints the unique variable.

Complexity Analysis:
- Time: O(1) per test case - Uses direct conditional statements.
- Space: O(1) - Constant auxiliary space.
"""

import sys 
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())

        if a == b:
            print(c)

        if b == c:
            print(a)

        if a == c:
            print(b)

if __name__ == "__main__":
    solve()