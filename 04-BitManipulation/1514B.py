"""
Day 143: Codeforces 1514B - AND 0, Sum Big
Topic: Math / Combinatorics / Modular Arithmetic
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`.
3. To make the bitwise AND of the array equal to 0, every bit position from 0 to k-1 must have a zero at that position in at least one element.
4. To maximize the overall sum while keeping the AND sum 0, we want each of the k bit positions to have a 0 in only one chosen element, while all other elements have a 1.
5. For each of the k bit positions, any of the n elements can be chosen to contribute that 0 ($n$ choices). 
6. Since there are k independent bit positions, we multiply the choices: $n \times n \times \dots \times n$ ($k$ times), which simplifies to $n^k$. Compute $(n^k) \pmod{10^9 + 7}$.

Complexity Analysis:
- Time: O(\log K) per test case - using fast modular exponentiation via `pow(n, k, MOD)`.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    MOD = 10**9 + 7
    for _ in range(t):
        n, k = map(int, input().split())
        print(pow(n, k, MOD))

if __name__ == "__main__":
    solve()