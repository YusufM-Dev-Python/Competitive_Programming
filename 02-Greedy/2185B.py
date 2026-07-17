"""
Day 102: 2185B - Maximum Potential
Topic: Greedy / Math
Goal: Maximize the total sum or outcome based on array elements.

Logic:
1. The problem essentially boils down to an observation: if you can perform 
   operations to replace elements, the most impactful element is the 
   maximum value present in the array.
2. By multiplying the maximum element by the number of elements (n), you 
   effectively distribute that maximum value across the entire array 
   to reach the theoretical upper bound of the sum.
3. This is a classic "Greedy Observation" problem where the code is 
   deceptively simple because the logic relies on finding the global 
   maximum rather than simulating complex operations.

Complexity Analysis:
- Time: O(N) per test case - One pass to find the maximum element.
- Space: O(1) - Aside from input storage.
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

        # The core greedy observation: 
        # The best possible outcome is achieved by utilizing the 
        # maximum element 'n' times.
        print(max(arr) * n)

if __name__ == "__main__":
    solve()