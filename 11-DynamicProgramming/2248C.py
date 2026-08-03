"""
Day 118: 2248C - Maximize the Score (Dynamic Programming with First Occurrence)
Topic: Dynamic Programming / Hash Maps
Goal: Compute the maximum score path by leveraging previous states when matching elements reappear.

Logic:
1. State Definition: `dp[i]` represents the maximum score achievable using prefix length `i`.
2. Base Transition: By default, extending the sequence adds 1 to the previous state (`dp[i] = dp[i-1] + 1`).
3. Optimization via First Occurrence: If the current element has appeared before at index `L` (`first_occ[val]`), 
   we can form a valid segment from `L` to `i`, yielding a contribution of `length * length + dp[L - 1]`. 
   We take the maximum between the linear continuation and this segment choice.
4. If it's the first time seeing the element, we record its index for future segment jumps.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Single pass through the array with dictionary lookups.
- Space: $\mathcal{O}(N)$ to store the DP array and position tracking map.
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
        
        m = len(arr)
        first_occ = {}
        dp = [0] * (m + 1)
        
        for i in range(1, m + 1):
            val = arr[i - 1]
            # Default transition: extend previous score by 1
            dp[i] = dp[i - 1] + 1
            
            # If element has appeared previously, check segment jump option
            if val in first_occ:
                L = first_occ[val]
                length = i - L + 1
                dp[i] = max(dp[i], length * length + dp[L - 1])
            else:
                first_occ[val] = i
                
        print(dp[m])

if __name__ == "__main__":
    solve()