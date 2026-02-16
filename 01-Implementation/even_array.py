"""
Day 16: Even Array (Codeforces 1367B)
Problem Link: https://codeforces.com/contest/1367/problem/B

Logic:
An array is 'good' if for every index i, (i % 2 == arr[i] % 2).
To fix a 'bad' array with minimum swaps:
1. Identify mismatches:
   - bad_even: Index is even, but value is odd.
   - bad_odd: Index is odd, but value is even.
2. Each swap can fix exactly one 'bad_even' and one 'bad_odd' simultaneously.
3. If bad_even == bad_odd, we need exactly 'bad_even' swaps.
4. If they aren't equal, it's impossible to fix (return -1).

Complexity Analysis:
- Time: O(N) - A single pass through the array.
- Space: O(N) - To store the input array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        bad_odd = 0
        bad_even = 0

        for i in range(n):
            # Check for parity mismatch between index and value
            if i % 2 == 0:
                if arr[i] % 2 != 0:
                    bad_even += 1
            else:
                if arr[i] % 2 == 0:
                    bad_odd += 1
        
        # We can only fix the array if we have an equal number 
        # of even-index errors and odd-index errors to swap.
        if bad_even != bad_odd:
            print(-1)
        else:
            # Each swap fixes one of each, so the count is the answer.
            print(bad_even)

if __name__ == "__main__":
    solve()