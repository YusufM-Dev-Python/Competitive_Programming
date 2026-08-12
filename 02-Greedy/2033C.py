"""
Day 126: 2033C - Sakurako's Field Trip (Greedy Swapping Strategy)
Topic: Greedy / Two Pointers / Arrays
Goal: Minimize the number of adjacent identical elements in an array 
      by deciding whether to swap symmetric pairs from outside inward.

Logic:
1. Symmetry & Swapping: Elements at index `i` and `n - 1 - i` form symmetric pairs. 
   Swapping them affects the adjacency costs at both ends simultaneously.
2. Cost Evaluation: For each step, we compare `cost_stay` (keeping elements as they are) 
   versus `cost_swap` (swapping them).
3. Greedy Decision: If swapping strictly decreases the local disturbance score, we execute the swap; 
   otherwise, we leave them in place. Finally, we count all remaining adjacent identical elements.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Linear passes to evaluate pairs and count matching neighbors.
- Space: $\mathcal{O}(N)$ to store the array elements.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        same = 0

        # Greedily evaluate swaps from the center outward or vice versa
        for i in range(1, n // 2):
            cost_stay = (arr[i] == arr[i-1]) + (arr[n-i-1] == arr[n-i])
            cost_swap = (arr[n-i-1] == arr[i-1]) + (arr[i] == arr[n-i])

            if cost_swap < cost_stay:
                arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
            else:
                continue

        # Count total adjacent matching elements after greedy adjustments
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                same += 1

        print(same)

if __name__ == "__main__":
    solve()