"""
Day 105: 2225C - Complex String Transformation
Topic: Dynamic Programming
Goal: Find the minimum cost to make two strings equivalent through operations.

Logic:
1. State Definition:
   - 'prev1': The minimum cost to align the strings up to the previous index (i-1).
   - 'prev2': The minimum cost to align the strings up to two indices back (i-2).
2. Transitions:
   - Vertical Cost: If s1[i] != s2[i], it costs 1 to align them vertically.
   - Horizontal Cost: If we transition horizontally, we consider the changes 
     between current characters and the previous ones in both strings: 
     (s1[i] != s1[i-1]) + (s2[i] != s2[i-1]).
   - Greedy Choice: At each index, choose the minimum of aligning vertically 
     or transitioning horizontally.
3. This is an elegant DP approach that reduces memory usage to O(1) space 
   by only tracking the two previous states.

Complexity Analysis:
- Time: O(N) per test case - One linear pass through the strings.
- Space: O(1) - Only storing a few integer states.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        s1 = input()
        s2 = input()

        # prev2: Cost up to index i-2
        # prev1: Cost up to index i-1
        prev2 = 0 
        prev1 = 1 if s1[0] != s2[0] else 0 
        
        for i in range(1, n):
            # Option 1: Vertical alignment at current index
            vertical_cost = 1 if s1[i] != s2[i] else 0
            path1_total = prev1 + vertical_cost
            
            # Option 2: Horizontal transition from previous index
            horizontal_cost = (s1[i] != s1[i-1]) + (s2[i] != s2[i-1])
            path2_total = prev2 + horizontal_cost
            
            # DP State update
            current = min(path1_total, path2_total)
            
            prev2 = prev1
            prev1 = current
            
        print(prev1)

if __name__ == "__main__":
    solve()