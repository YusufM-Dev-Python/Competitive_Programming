"""
Day 106 (Part 3): 2173B - Dynamic Programming State Tracking
Topic: Dynamic Programming / Greedy State Management
Goal: Track the evolution of potential min/max bounds across elements to find the optimal result.

Logic:
1. Initialization: We start with a baseline value `k = 0`, establishing initial 
   upper (`max_k`) and lower (`min_k`) bounds based on the first elements of arrays `a` and `b`.
2. State Transitions: For each subsequent step from index 1 to n-1, we evaluate multiple 
   potential paths (`path_1` to `path_4`) accounting for the interactions with `a[i]` and `b[i]`.
3. Bounding: At each step, we aggressively narrow down or expand our tracking state by 
   taking the `max` and `min` of these paths, ensuring we carry forward the optimal extreme states.
4. This avoids exploring an exponential number of choices by collapsing the state space 
   down to just tracking the current active minimum and maximum bounds.

Complexity Analysis:
- Time: O(N) per test case - Single linear pass through the arrays.
- Space: O(N) to store the input arrays `a` and `b`.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        k = 0

        # Establish initial bounds using the first element
        k_a = k - a[0]
        k_b = b[0] - k

        max_k = max(k_a, k_b)
        min_k = min(k_a, k_b)

        # Iterate through the remaining elements maintaining min/max tracking states
        for i in range(1, n):
            path_1 = max_k - a[i]
            path_2 = min_k - a[i]

            path_3 = b[i] - max_k
            path_4 = b[i] - min_k

            new_max_k = max(path_1, path_2, path_3, path_4)
            new_min_k = min(path_1, path_2, path_3, path_4)

            max_k = new_max_k
            min_k = new_min_k

        print(max_k)
    
if __name__ == "__main__":
    solve()