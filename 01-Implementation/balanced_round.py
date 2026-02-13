"""
Day 14: Balanced Round (Codeforces 1850D)
Problem Link: https://codeforces.com/contest/1850/problem/D

Logic:
To minimize deletions, we must maximize the number of problems we keep. 
A round is balanced if the difference between adjacent problems is <= k. 
1. Sort the problems: This allows us to check the smallest possible differences.
2. Find the Longest Subsegment: Traverse the sorted array and count the longest 
   streak where a[i+1] - a[i] <= k.
3. Result: n - max_streak (total problems minus the ones we can keep).

Complexity Analysis:
- Time: O(N log N) due to the sorting step. The scan is O(N).
- Space: O(N) to store the input array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Sorting is essential to group numbers with minimum differences
        a.sort()
        
        max_streak = 1
        current_streak = 1
        
        # Edge case: only one problem is always balanced
        if n == 1:
            print(0)
            continue
            
        for i in range(n - 1):
            # Check if the next problem fits the balance condition
            if a[i+1] - a[i] <= k:
                current_streak += 1
            else:
                # Condition broken: record streak and reset
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        
        # Final check to catch the streak if it lasted until the last element
        max_streak = max(max_streak, current_streak)
        
        # The problems to delete are the ones not part of the longest streak
        print(n - max_streak)

if __name__ == "__main__":
    solve()