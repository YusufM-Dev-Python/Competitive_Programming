"""
Day 125: Array Transformation & Prefix Sum Gain Optimization
Topic: Prefix Sums / Arrays
Goal: Compute maximum possible gain by evaluating localized prefix/suffix updates 
      combined with prefix sum arrays.

Logic:
1. Prefix Sum Construction: Build a prefix sum array `pf` in $\mathcal{O}(N)$ time to allow 
   fast range sum queries.
2. Tracking Optimal Left States: Maintain `max_L` evaluating components like `pf[i-1] - (i * i) + i` 
   dynamically as we loop through index bounds.
3. Combining Gains: Evaluate `current_R` contributions and aggregate `max_L + current_R` 
   to find the absolute maximum overall gain added to the `original_sum`.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Single linear pass using precalculated prefix sums.
- Space: $\mathcal{O}(N)$ to store array elements and prefix tracking tables.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        pf = [0] * (n + 1)

        # Step 1: Build prefix sums
        for i in range(n):
            pf[i+1] = pf[i] + arr[i]

        original_sum = pf[n]
        max_gain = 0 
        max_L = float('-inf')

        # Step 2: Iterate to find optimal combined left and right contributions
        for i in range(1, n + 1):
            current_L = pf[i-1] - (i * i) + i
            if current_L > max_L:
                max_L = current_L
                
            current_R = (i * i) + i - pf[i]

            current_gain = max_L + current_R
            if current_gain > max_gain:
                max_gain = current_gain

        print(original_sum + max_gain)

if __name__ == "__main__":
    solve()