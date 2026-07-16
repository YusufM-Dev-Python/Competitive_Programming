"""
Day 101: 2170B - Greedy Balancing
Topic: Greedy / Implementation
Logic:
1. The goal is to determine the optimal count based on the number of positive 
   elements vs. the total sum constraint.
2. We count how many elements are strictly greater than zero (`b_non_0`).
3. We calculate the effective remaining capacity using `sum_b - n + 1`.
4. The result is the minimum of these two values, ensuring we satisfy both 
   the existence constraint and the total sum limit.

Complexity Analysis:
- Time: O(N) - Single pass to count non-zero elements and calculate sum.
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
        b = list(map(int, input().split()))

        # Count positive elements and total sum
        b_non_0 = sum(1 for x in b if x > 0)
        sum_b = sum(b)

        # Output the limiting constraint
        print(min(b_non_0, sum_b - n + 1))

if __name__ == "__main__":
    solve()