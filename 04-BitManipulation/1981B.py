"""
Day 149: Codeforces 1981B - Bitwise Operations / Range OR
Topic: Bit Manipulation / Math
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `m`. The problem deals with values in the range $[max(0, n - m), n + m]$.
3. Find the XOR difference between the lower bound `l` and upper bound `r` to identify differing bits.
4. Determine the Most Significant Bit (MSB) position using `bit_length() - 1`.
5. Construct a mask that covers all bits up to that MSB position, apply it via bitwise OR with `r`, and print the maximized result.

Complexity Analysis:
- Time: O(1) per test case - constant time bitwise operations.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        l = max(0, n - m)
        r = n + m

        diff = l ^ r
        msb = diff.bit_length() - 1

        mask = (1 << (msb + 1)) - 1
        ans = r | mask

        print(ans)

if __name__ == "__main__":
    solve()