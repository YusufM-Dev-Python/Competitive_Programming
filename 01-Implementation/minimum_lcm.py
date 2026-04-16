"""
Day 58: Minimum LCM (Codeforces 1765M)
Logic:
1. We need to find a, b such that a + b = n and LCM(a, b) is minimized.
2. Mathematically, minimizing LCM is the same as maximizing GCD.
3. The largest possible GCD(a, b) where a+b=n is the largest proper divisor of n.
4. We find the smallest divisor 'i' (>=2) of n. The largest divisor is then n // i.
5. If no divisor is found up to sqrt(n), n is prime, and a=1, b=n-1.

Complexity Analysis:
- Time: O(sqrt(N)) per test case.
- Space: O(1).
"""

import sys
import math

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n_str = input()
        if not n_str: continue
        n = int(n_str)

        # Default: if n is prime, the largest proper divisor is 1
        a = 1

        # Find the smallest factor to get the largest proper divisor
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                # n // i is the largest proper divisor
                a = n // i
                break
        
        # b is the remainder
        b = n - a
        print(f"{a} {b}")

if __name__ == "__main__":
    solve()