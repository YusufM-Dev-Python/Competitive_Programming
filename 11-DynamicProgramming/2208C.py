"""
Day 120: 2208C - Probability & Backward Dynamic Programming
Topic: Dynamic Programming / Probability
Goal: Maximize expected outcome or value by making optimal keep/leave decisions 
      from back to front with probability scaling.

Logic:
1. Backward DP: Working backwards from the last element allows us to accumulate future expectations.
2. Choice Analysis: At each step `i`, we decide between:
   - `leave`: Skipping the current item, retaining the accumulated value from future steps (`ans`).
   - `keep`: Taking the current cost `c[i]` plus the future expectation scaled by the failure probability `(1.0 - p[i] / 100.0)`.
3. Optimal Substructure: `ans = max(leave, keep)` ensures we take the optimal choice at every state.
4. Precision Output: Formatted printing `f"{ans:.9f}"` handles floating-point probability outputs cleanly.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Single linear pass backwards through the items.
- Space: $\mathcal{O}(N)$ to store cost and probability arrays.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())

        c = []
        p = []
        for _ in range(n):
            ci, pi = map(int, input().split())
            c.append(ci)
            p.append(pi)
            
        ans = 0.0
        
        # Backward DP traversal
        for i in range(n - 1, -1, -1):
            leave = ans 
            keep = c[i] + ans * (1.0 - p[i] / 100.0)
            ans = max(leave, keep)

        print(f"{ans:.9f}")

if __name__ == "__main__":
    solve()