"""
Day 100: Milestone Reached! (Contest Pattern Logic)
Topic: Implementation / Greedy
Logic:
1. Identify the longest contiguous chain of '#' characters in the string.
2. The problem requires a calculation based on this maximum length (max_chain).
3. Using ceiling division (max_chain // 2 + (1 if max_chain % 2 != 0 else 0)), 
   you derive the required result efficiently.

Complexity Analysis:
- Time: O(N) - Single pass through the string to find the maximum chain.
- Space: O(1) - Using constant space for counters.
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

        max_chain = 0
        curr_chain = 0

        for char in s:
            if char == '#':
                curr_chain += 1
            else:
                curr_chain = 0
            max_chain = max(max_chain, curr_chain)
        
        # Calculate result based on chain length
        if max_chain == 0:
            print(0)
        else:
            # Equivalent to ceil(max_chain / 2)
            print((max_chain + 1) // 2)

if __name__ == "__main__":
    solve()