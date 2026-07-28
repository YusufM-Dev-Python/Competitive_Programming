"""
Day 113: 1178B - WOW Factor
Topic: Strings / Prefix-Suffix Aggregation
Goal: Count the number of subsequences that form "WOW", where each 'W' is represented 
      by a pair of adjacent 'v's ("vv"), and the middle is 'o'.

Logic:
1. Understanding "WOW": A "WOW" structure consists of `[W] [o] [W]`, where each 'W' 
   is a pair of consecutive 'v's (`"vv"`).
2. Prefix & Suffix Strategy: 
   - We need to know how many `"vv"` pairs exist to the left of any given index and to the right.
   - In your logic, `t_w` counts the total number of `"vv"` pairs across the entire string.
   - As we iterate through to find `'o'`, `l_w` tracks the accumulated `"vv"` pairs to the left, 
   - and `t_w - l_w` gives the remaining `"vv"` pairs to the right.
3. Combination Counting: For every `'o'` at index `i`, the total number of "WOW" configurations 
   using this specific `'o'` as the center is `(pairs_on_left) * (pairs_on_right)`.

Complexity Analysis:
- Time: O(N) - Linear scans to count `"vv"` pairs and evaluate positions.
- Space: O(N) to store the input string.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    s_input = input()
    if not s_input: return
    s = s_input

    t_w = 0
    l_w = 0
    total = 0

    # Step 1: Count total number of "vv" pairs (total 'W' components available)
    for i in range(1, len(s)):
        if s[i] == 'v' and s[i-1] == 'v':
            t_w += 1

    # Step 2: Iterate again to evaluate each 'o' as the center of "WOW"
    for i in range(1, len(s)):
        if s[i] == 'v' and s[i-1] == 'v':
            l_w += 1
        elif s[i] == 'o':
            # For each 'o', multiply choices on the left (l_w) by choices on the right (t_w - l_w)
            total += ((t_w - l_w) * l_w)

    print(total)
    
if __name__ == "__main__":
    solve()