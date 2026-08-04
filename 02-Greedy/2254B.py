"""
Day 119 (Part 2): Contest String Reduction Logic
Topic: Strings / Greedy Simulation
Goal: Compute the minimal compressed string length by evaluating potential character 
      reductions across adjacent matching neighborhoods.

Logic:
1. Initial Segments: Count the initial number of distinct alternating blocks in the string (`initial_len`).
2. Neighborhood Reduction Scan: Examine triplets `(s[i-1], s[i], s[i+1])` to find the maximum 
   possible reduction (`max_reduction`) by collapsing characters under specific match conditions.
3. Final Evaluation: Subtract the maximum reduction from the initial block count to get the optimal result.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Linear scan across the string length.
- Space: $\mathcal{O}(N)$ to store the list representation of the input string.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        s = input()
        
        # Calculate initial block segments
        initial_len = 1
        for i in range(1, n):
            if s[i] != s[i-1]:
                initial_len += 1

        # Check maximum possible reductions based on local patterns
        max_reduction = 0
        for i in range(1, n - 1):
            if s[i-1] == s[i+1] and s[i] != s[i-1]:
                max_reduction = max(max_reduction, 2)
            elif s[i] != s[i-1] and s[i] != s[i+1]:
                max_reduction = max(max_reduction, 1)
                
        print(initial_len - max_reduction)

if __name__ == "__main__":
    solve()