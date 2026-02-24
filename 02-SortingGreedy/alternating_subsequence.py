"""
Day 23: Alternating Subsequence (Codeforces 1343C)
Problem Link: https://codeforces.com/contest/1343/problem/C

Logic:
1. We need an alternating subsequence of maximum length. The length is 
   simply the count of sign-alternating "blocks" in the array.
2. To maximize the sum, we must pick the largest element from each 
   consecutive block of numbers with the same sign.
3. We iterate once: 
   - If sign stays the same, update the current block's maximum.
   - If sign changes, add the previous max to our total and start a new block.

Complexity Analysis:
- Time: O(N) - Single pass through the array per test case.
- Space: O(N) - To store the input array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        total_sum = 0
        # Initialize the first block's maximum with the first element
        current_block_max = arr[0] 

        for i in range(1, n):
            # Check if the sign has changed compared to the previous element
            if (arr[i] > 0) != (arr[i-1] > 0): 
                # Sign flipped: Add the best candidate from the finished block
                total_sum += current_block_max
                # Start the new block
                current_block_max = arr[i]
            else:
                # Same sign: Keep the largest value in this block
                current_block_max = max(current_block_max, arr[i])
        
        # Don't forget to add the maximum of the final block
        total_sum += current_block_max 
        print(total_sum)

if __name__ == "__main__":
    solve()