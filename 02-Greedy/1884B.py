"""
Day 130 (Part 2): 1884B - Haunted House (Trailing Zero Positions & Swaps)
Topic: Greedy / Strings
Goal: Find the minimum number of adjacent swaps required to make the binary prefix 
      divisible by 2^k for each length k from 1 to n.

Logic:
1. Identifying Target Zeros: We scan the string from right to left to collect the 
   original indices of all '0' characters. Moving a '0' to the rightmost available 
   positions allows us to form powers of 2.
2. Cumulative Swaps: For each position from 1 to n, we calculate how far the next available 
   '0' needs to travel to reach the target slot from the right edge.
3. Fallback Condition: If there aren't enough zeros available to satisfy length `k`, 
   we output `-1` for that and all subsequent lengths.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Single passes to collect zero indices and calculate swaps.
- Space: $\mathcal{O}(N)$ to store the positions array and answer buffer.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        s = input()

        zeroes = []
        ans = [-1] * n
        current_swap = 0

        # Step 1: Collect indices of all '0' characters from right to left
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                zeroes.append(i)
        
        # Step 2: Compute cumulative swap distances for each target position from the right
        for i in range(n):
            tar = n - i - 1
            if i < len(zeroes):
                current_swap += tar - zeroes[i]
                ans[i] = current_swap
            else:
                break

        print(*ans)

if __name__ == "__main__":
    solve()