"""
Day 167: Codeforces 2283C - Big XOR
Topic: Bit Manipulation / Greedy / Constructive

Question Extraction:
- Given an integer n and the array a = [1, 2, ..., n].
- We may double any subset of elements (each at most once), giving array b.
- Let k = OR of all elements of a, and m = XOR of all elements of b.
- Choose which elements to double (d_i = 1 or 0) so that m >= 2k.

Key Observations:
- Let h = highest set bit of n. Then k = 2^(h+1) - 1 and 2k = 2^(h+2) - 2.
- Every element of b is <= 2n < 2^(h+2), so m <= 2^(h+2) - 1 = 2k + 1.
- So m >= 2k forces m to be 2k or 2k + 1, i.e. bits 1..h+1 of m must all
  be 1 (bit 0 is free).
- Doubling x changes m by x ^ 2x. For x = 2^(j-1) this toggles exactly
  bits j-1 and j, so the highest changed bit is j.

Approach (Greedy, top bit down):
1. Compute m = 1 ^ 2 ^ ... ^ n (nothing doubled yet).
2. For j = h+1 down to 1:
   - If bit j of m is 0, double the element x = 2^(j-1) and update
     m ^= x ^ (x << 1).
3. Fixing bit j only disturbs bit j-1 (handled next), and bits above j
   are never touched again, so earlier work is never undone.
4. x = 2^(j-1) <= 2^h <= n always exists, and each power of two is used
   at most once.

Logic:
1. Read t test cases.
2. For each test, read n and build a = [1, 2, ..., n].
3. Compute k (OR of a) and m (XOR of a).
4. Compute h = n.bit_length() - 1 and initialise d = [0] * (n + 1).
5. Loop j from h+1 down to 1, doubling 2^(j-1) whenever bit j of m is 0.
6. Print d[1:] separated by spaces.

Complexity:
- Time: O(n) per test case (O(n) for the XOR pass, O(log n) for the greedy
  loop). Total O(sum of n) <= 2 * 10^5.
- Space: O(n) for the array and the indicator list.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(range(1, n + 1))

        k = 0
        for x in a:
            k |= x

        m = 0
        for y in a:
            m ^= y

        h = n.bit_length() - 1
        d = [0] * (n + 1)

        for j in range(h + 1, 0, -1):
            if not (m >> j) & 1:
                x = 1 << (j - 1)
                d[x] = 1
                m ^= x ^ (x << 1)

        # m is now 2k or 2k + 1, so m >= 2k holds
        assert m >= 2 * k

        print(*d[1:])


if __name__ == "__main__":
    solve()