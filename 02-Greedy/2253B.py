"""
Day 122 (Part 2): 2253B - Array Pattern Matching & Pair Reduction
Topic: Arrays / Greedy Analysis
Goal: Analyze adjacent duplicate pairs and structural groupings to compute 
      the minimal or optimal length under strict neighbor conditions.

Logic:
1. Total Pairs Count: First, count all adjacent identical pairs (`total_pairs`) in the array.
2. Neighborhood Pattern Search: Check for specific multi-element patterns (e.g., alternating blocks 
   where pairs repeat with separation) to flag complex configurations (`has_adj_pairs`).
3. Conditional Reduction: Depending on whether complex patterns exist, evaluate deletion flags 
   to determine how many pair reductions can be effectively applied (`n - (total_pairs - delete)`).

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Linear passes to scan pairs and neighborhood windows.
- Space: $\mathcal{O}(N)$ to store the array elements.
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

        # Count total adjacent pairs
        total_pairs = 0
        for i in range(n - 1):
            if arr[i] == arr[i+1]:
                total_pairs += 1

        # Check for specific alternating adjacent duplicate structures
        has_adj_pairs = False
        for i in range(n - 3):
            if arr[i] == arr[i+1] and arr[i+1] != arr[i+2] and arr[i+2] == arr[i+3]:
                has_adj_pairs = True
                break

        # Compute optimal result based on structural classification
        if has_adj_pairs:
            print(n - (total_pairs - 2))
        else:
            delete = 0
            for i in range(n - 1):
                if arr[i] == arr[i+1]:
                    if i + 2 < n and arr[i+2] != arr[i]:
                        if i + 3 >= n or arr[i+3] != arr[i]:
                            delete = 1
                            break
        
                    if i - 1 >= 0 and arr[i-1] != arr[i]:
                        if i - 2 < 0 or arr[i-2] != arr[i]:
                            delete = 1
                            break

            print(n - (total_pairs - delete))

if __name__ == "__main__":
    solve()