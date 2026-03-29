"""
Day 43: Cut Ribbon (Codeforces 189A)
Problem Link: https://codeforces.com/contest/189/problem/A

Logic:
1. We need to maximize x + y + z such that a*x + b*y + c*z = n.
2. We can iterate through all possible values of x and y.
3. For each pair (x, y), calculate the remaining length: rem = n - (a*x + b*y).
4. If rem is non-negative and divisible by c, we found a valid z.
5. Track the maximum (x + y + z) found across all iterations.

Complexity Analysis:
- Time: O(N^2 / (a*b)) - In the worst case O(N^2).
- Space: O(1) - No extra data structures needed.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line = input().split()
    if not line: return
    n, a, b, c = map(int, line)
    
    ans = 0
    # Iterate through possible number of pieces of length 'a'
    for x in range((n // a) + 1):
        # Iterate through possible number of pieces of length 'b'
        for y in range(((n - x * a) // b) + 1):
            
            len_used = (x * a) + (y * b)
            rem_len = n - len_used
            
            # Check if the remainder can be perfectly filled by pieces of length 'c'
            if rem_len >= 0 and rem_len % c == 0:
                z = rem_len // c
                ans = max(ans, x + y + z)
                
    print(ans)

if __name__ == "__main__":
    solve()