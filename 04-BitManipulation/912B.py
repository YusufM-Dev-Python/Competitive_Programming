"""
Day 153: Codeforces 912B - New Year's Eve (300th Solved Problem!)
Topic: Bit Manipulation / Greedy / Math
Logic:
1. Read inputs `n` and `k`.
2. If `k == 1`, we can only pick one number, so the maximum possible XOR sum is simply `n`.
3. If `k > 1`, we can leverage numbers up to the highest bit length of `n`. By choosing numbers that saturate all bits up to the Most Significant Bit (MSB), we can achieve the maximum possible value for a given bit length, which is $2^{\text{bit\_length}} - 1$.

Complexity Analysis:
- Time: O(1) - constant time bit-length calculation.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, k = map(int, input().split())

    count = n.bit_length()
    print(n) if k == 1 else print(2**count - 1)

if __name__ == "__main__":
    solve()