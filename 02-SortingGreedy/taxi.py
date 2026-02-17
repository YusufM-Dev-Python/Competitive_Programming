"""
Day 17: Taxi (Codeforces 158A)
Problem Link: https://codeforces.com/contest/158/problem/A

Logic:
This is a Greedy problem solvable with Two Pointers.
1. Sort the groups: This allows us to pair the largest groups with the smallest.
2. Two Pointers: 
   - 'r' points to the largest group (right side).
   - 'l' points to the smallest group (left side).
3. Process: Every taxi must take the largest available group (arr[r]). 
   After they board, we check if any of the smallest groups (arr[l]) 
   can fit in the remaining 'rem_space'.

Complexity Analysis:
- Time: O(N log N) due to sorting. The two-pointer scan is O(N).
- Space: O(N) to store the group sizes.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Number of groups
    n_str = input()
    if not n_str: return
    n = int(n_str)

    # Sizes of each group
    arr = list(map(int, input().split()))
    
    # Sorting is necessary for the two-pointer greedy strategy
    arr.sort()
    
    l = 0
    r = n - 1
    taxis = 0

    while l <= r:
        # Every iteration represents one taxi
        taxis += 1
        
        # Start by putting the largest remaining group in the taxi
        rem_space = 4 - arr[r]
        r -= 1
        
        # Try to fit the smallest groups into the remaining space of this taxi
        while l <= r and rem_space >= arr[l]:
            rem_space -= arr[l]
            l += 1

    print(taxis)

if __name__ == "__main__":
    solve()