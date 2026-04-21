"""
Day 63: Sum of Odd Integers (Codeforces 1327A)
Logic:
1. Parity: The sum of K odd numbers is even if K is even, and odd if K is odd.
   Therefore, n % 2 must equal k % 2.
2. Magnitude: To use K distinct odd integers, the smallest sum possible 
   is 1 + 3 + 5 + ... + (2k-1) = k^2.
3. If n >= k^2 and parities match, the answer is "YES".

Complexity Analysis:
- Time: O(1) per test case.
- Space: O(1).
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n, k = map(int, input().split())

        # Check parity and minimum possible sum (k*k)
        if n % 2 == k % 2 and n >= k * k:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()