"""
Day 111: Contest Problem A - Parity and Alternating Extremes
Topic: Implementation / Greedy Logic
Goal: Determine if the array structure meets the alternating value criteria 
      based on odd/even index bounds.

Logic:
1. Parity Check: If the length 'n' is odd, the problem conditions cannot be satisfied ("NO").
2. Index-based Tracking: 
   - Even indices track the minimum threshold (`min_ce`).
   - Odd indices track the maximum threshold (`max_ce`).
3. Validation: Compare the extreme values (`min_ce > max_ce + 1`) to verify if the 
   interleaved condition holds true for a "YES" or "NO" outcome.

Complexity Analysis:
- Time: O(N) per test case - Single pass through the array elements.
- Space: O(N) to store the input array.
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

        max_ce = 0
        min_ce = float('inf')

        # If length is odd, configuration is automatically invalid
        if n % 2 != 0:
            print("NO")
        else:
            # Track values at alternating indices
            for i in range(n):
                if i % 2 == 0:
                    min_ce = min(min_ce, arr[i])
                else:
                    max_ce = max(max_ce, arr[i])

            # Check boundary conditions
            if min_ce > max_ce + 1:
                print("YES")
            else:
                print("NO")
            
if __name__ == '__main__':
    solve()