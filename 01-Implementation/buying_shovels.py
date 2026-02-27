"""
Day 26: Buying Shovels (Codeforces 1360D)
Problem Link: https://codeforces.com/contest/1360/problem/D

Logic:
We want to find the largest divisor 'd' of 'n' such that 'd <= k'.
The answer will then be n // d.
Since n is up to 10^9, we find divisors in O(sqrt(n)) time.
For each 'i' from 1 to sqrt(n):
- if n % i == 0:
    - check if i <= k (candidate divisor)
    - check if (n // i) <= k (candidate divisor)

Complexity Analysis:
- Time: O(T * sqrt(N)) - Efficient enough for N=10^9 and T=100.
- Space: O(1).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n, k = map(int, input().split())

        # If we can buy all shovels in one shovel-type package
        if n <= k:
            print('1')
            continue

        ans = n
        i = 1
        # O(sqrt(N)) divisor finding
        while i * i <= n:
            if n % i == 0:
                # 'i' is a divisor
                if i <= k:
                    ans = min(ans, n // i)
                
                # 'n // i' is also a divisor
                other_divisor = n // i
                if other_divisor <= k:
                    ans = min(ans, i)
            i += 1
        print(ans)

if __name__ == "__main__":
    solve()