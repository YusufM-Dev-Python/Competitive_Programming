"""
Day 112: 701C - They Are Everywhere (Sliding Window)
Topic: Two Pointers / Sliding Window / Hash Maps
Goal: Find the length of the shortest contiguous substring that contains 
      all unique characters present in the main string.

Logic:
1. Unique Character Target: First, find the total number of distinct characters 
   in the entire string (`uniq_elem = len(set(s))`).
2. Sliding Window Expansion: 
   - Expand the right pointer `r` to include characters in a frequency dictionary (`uniq`).
3. Shrinking Phase: 
   - While the frequency of the character at the left pointer `l` is strictly greater than 1, 
     we can safely shrink the window from the left (`uniq[s[l]] -= 1`, `l += 1`) 
     without losing any unique character types.
4. Optimal Update: 
   - If the current window contains all unique elements (`len(uniq) == uniq_elem`), 
     update our `min_len` with `r - l + 1`.

Complexity Analysis:
- Time: O(N) - Each character is processed at most twice (once by `r`, once by `l`).
- Space: O(K) where K is the number of distinct characters in the string (at most 52 for letters).
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n_input = input()
    if not n_input: return
    n = int(n_input)
    s = input()

    uniq = {}
    uniq_elem = len(set(s))  # Total distinct characters to cover
    min_len = float('inf')

    l = 0
    for r in range(n):
        # Expand window by adding current character to frequency map
        uniq[s[r]] = uniq.get(s[r], 0) + 1
    
        # Shrink window from the left as long as we have redundant characters
        while uniq[s[l]] > 1:
            uniq[s[l]] -= 1
            l += 1

        # If the window contains all unique elements, update the minimum length
        if len(uniq) == uniq_elem:
            min_len = min(min_len, r - l + 1)

    print(min_len)
        
if __name__ == "__main__":
    solve()