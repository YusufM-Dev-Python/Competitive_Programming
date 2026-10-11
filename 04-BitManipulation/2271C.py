"""
Day 155: Codeforces 2271C - Gray Code Sequence Construction
Topic: Constructive / Bit Manipulation / Gray Code
Logic:
1. Read the number of test cases `t`.
2. For each test case, read integer `n`.
3. Determine the bit length `b` required to cover the sequence range.
4. Generate Gray code values using `i ^ (i >> 1)` and duplicate them to form a prefix sequence (`pref`).
5. Derive the final array `arr` using adjacent XOR differences (`pref[i] ^ pref[i-1]`).
6. Print the length of the array and the elements.

Complexity Analysis:
- Time: O(2^B) per test case - proportional to the Gray code sequence length generated based on bit length.
- Space: O(2^B) - to store the prefix and output arrays.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        b = n.bit_length()
        pref = []
        for i in range(1 << b):
            g = i ^ (i >> 1)
            pref.append(g)
            pref.append(g)

        arr = [pref[i] ^ pref[i-1] for i in range(1, len(pref))]

        print(len(arr))
        print(*arr)

if __name__ == "__main__":
    solve()