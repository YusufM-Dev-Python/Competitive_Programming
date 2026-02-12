"""
Day 13: Blank Space (Codeforces 1829B)
Problem Link: https://codeforces.com/contest/1829/problem/B

Logic:
We are looking for the longest 'blank space' (consecutive zeros).
By iterating through the array:
1. Increment 'curr' every time we encounter a 0.
2. Reset 'curr' to 0 the moment we hit a 1 (breaking the streak).
3. Use max_streak to keep track of the highest 'curr' value reached.

Complexity Analysis:
- Time: O(N) - Single linear scan of the array.
- Space: O(1) - Constant space (two integer variables).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)

    for _ in range(t):
        n = int(input()) # Length of the array
        arr_a = list(map(int, input().split()))
        
        curr = 0
        max_streak = 0

        # Linear scan through the binary array
        for i in arr_a:
            if i == 0:
                # Found a zero, increment the current streak
                curr += 1
            else:
                # Found a one, the streak is broken - reset to zero
                curr = 0
            
            # Record the highest streak encountered
            if curr > max_streak:
                max_streak = curr

        print(max_streak)

if __name__ == "__main__":
    solve()