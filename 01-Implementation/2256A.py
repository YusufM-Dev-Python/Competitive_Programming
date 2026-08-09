"""
Day 123: 2256A - Sorting and Range Constraint Logic
Topic: Implementation / Math
Goal: Evaluate relationships between three sorted variables and apply optimal 
      range arithmetic to determine the result.

Logic:
1. Input & Sorting: Read the three values `a`, `b`, `c`, append them to an array, 
   and sort them in descending order (`arr[0]` is the largest).
2. Range Checking: Calculate the sum of the two smaller elements (`range_checker = arr[1] + arr[2]`).
3. Conditional Evaluation: 
   - If the sum of the two smaller elements is less than the largest element, 
     compute the result using `range_checker - arr[2]`.
   - Otherwise, apply the alternate difference condition `arr[0] - arr[2]`.

Complexity Analysis:
- Time: $\mathcal{O}(1)$ per test case - Sorting a fixed array of 3 elements takes constant time.
- Space: $\mathcal{O}(1)$ - Constant auxiliary space.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        a, b, c = map(int, input().split())
        arr = [a, b, c]

        # Sort descending to isolate the largest element at arr[0]
        arr.sort(reverse=True)
        range_checker = arr[1] + arr[2]
        
        # Apply conditional constraints based on range bounds
        if range_checker < arr[0]:
            print(range_checker - arr[2])
        else:
            print(arr[0] - arr[2])

if __name__ == "__main__":
    solve()