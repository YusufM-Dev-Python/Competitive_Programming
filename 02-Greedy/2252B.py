"""
Day 121 (Part 2): 2252B - Binary String Analysis & Deletions
Topic: Strings / Greedy Simulation
Goal: Analyze binary string counts and adjacent repetition blocks to determine 
      the minimal or optimal cost metric under constraint conditions.

Logic:
1. Counting Totals: Count total occurrences of '0's and '1's to ensure overall balance.
2. Consecutive Blocks: Track adjacent identical pairs (`del_0` for consecutive '0's, `del_1` for consecutive '1's).
3. Conditional Evaluation:
   - If total counts differ by more than 2, output `-1`.
   - If consecutive block differences are within 1, return the combined deletions.
   - Otherwise, apply adjusted scaling formulas depending on which block type dominates.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Linear passes to count elements and analyze adjacent pairs.
- Space: $\mathcal{O}(N)$ to store the array of digits.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input()))

        total_0 = 0
        total_1 = 0

        del_0 = 0
        del_1 = 0

        # Step 1: Count total 0s and 1s
        for i in range(n):
            if arr[i] == 1:
                total_1 += 1
            else:
                total_0 += 1

        # Step 2: Count consecutive identical pairs
        for i in range(1, n):
            if arr[i] == arr[i-1] == 0:
                del_0 += 1
            elif arr[i] == arr[i-1] == 1:
                del_1 += 1

        # Step 3: Evaluate conditions and compute optimal output
        if abs(total_0 - total_1) > 2:
            print(-1)
        elif abs(del_1 - del_0) <= 1:
            print(del_1 + del_0)
        elif del_1 > del_0:
            print(2 * del_1 - 1)
        else:
            print(2 * del_0 - 1)

if __name__ == "__main__":
    solve()