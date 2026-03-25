"""
Day 39: Pair of Topics (Codeforces 1324D)
Problem Link: https://codeforces.com/contest/1324/problem/D

Logic:
1. Transform a_i + a_j > b_i + b_j  => (a_i - b_i) + (a_j - b_j) > 0.
2. Let c[i] = a[i] - b[i]. We need to find pairs (i, j) where c[i] + c[j] > 0 and i < j.
3. Sort array 'c'.
4. Use two pointers (left, right):
   - If c[left] + c[right] > 0, all elements from 'left' to 'right-1' 
     work with 'right'. Add (right - left) to score, decrement 'right'.
   - Otherwise, increment 'left'.

Complexity Analysis:
- Time: O(N log N) - Dominated by sorting.
- Space: O(N) - To store the difference array 'c'.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n_str = input()
    if not n_str: return
    n = int(n_str)

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Calculate differences
    c = [a[i] - b[i] for i in range(n)]
    c.sort()
    
    score = 0
    left = 0
    right = n - 1

    while left < right:
        if c[left] + c[right] > 0:
            # If the smallest and largest sum to > 0, 
            # then 'right' pairs with everything between 'left' and 'right-1'
            score += (right - left)
            right -= 1
        else:
            # Sum is too small, need a larger 'left' element
            left += 1

    print(score)

if __name__ == "__main__":
    solve()