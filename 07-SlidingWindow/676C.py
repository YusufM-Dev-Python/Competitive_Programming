"""
Day 108: 676C - Vasya and String (Sliding Window)
Topic: Two Pointers / Sliding Window / Strings
Goal: Find the maximum length of a substring containing only one type of character ('a' or 'b') 
      after changing at most 'k' characters.

Logic:
1. Budget-based Sliding Window: We want to find the longest window where the number of 
   characters different from our target character does not exceed 'k'.
2. First Pass (Target 'a'):
   - Expand the right pointer `r`. If `arr[r]` is not 'a', we spend 1 from our budget `bud`.
   - If `bud < 0`, shrink the window from the left (`l`) until our budget is restored.
   - Track the maximum length (`max_a`).
3. Second Pass (Target 'b'):
   - Repeat the exact same sliding window logic, but with 'b' as the target character, 
     tracking `max_b`.
4. Output: The final answer is `max(max_a, max_b)`.

Complexity Analysis:
- Time: O(N) - Each character is visited at most twice (once by `r`, once by `l`) for each pass.
- Space: O(N) to store the input string.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n_k_input = input()
    if not n_k_input: return
    n, k = map(int, n_k_input.split())
    arr = input()

    # -------------------------------------------------------------
    # Pass 1: Find the longest valid window making characters mostly 'a'
    # -------------------------------------------------------------
    bud = k
    max_a = 0
    tar_1 = 'a'
    l = 0

    for r in range(n):
        if arr[r] != tar_1:
            bud -= 1
            
        while bud < 0:
            if arr[l] == tar_1:
                l += 1
            else:
                bud += 1
                l += 1

        max_a = max(max_a, r - l + 1)

    # -------------------------------------------------------------
    # Pass 2: Find the longest valid window making characters mostly 'b'
    # -------------------------------------------------------------
    bud = k
    max_b = 0
    tar_2 = 'b'
    l = 0

    for r in range(n):
        if arr[r] != tar_2:
            bud -= 1

        while bud < 0:
            if arr[l] == tar_2:
                l += 1
            else:
                bud += 1
                l += 1

        max_b = max(max_b, r - l + 1)

    # Print the maximum length found between both passes
    print(max(max_a, max_b))
    
if __name__ == "__main__":
    solve()