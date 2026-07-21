"""
Day 106: 1272C - Yet Another Broken Keyboard
Topic: Strings / Combinatorics / Two Pointers
Goal: Find the total number of substrings that can be formed using only a 
      given set of allowed/valid characters.

Logic:
1. We iterate through the string of length 'n'.
2. If the current character is in our `valid_chars` set, we extend our current 
   contiguous block of valid characters (`curr_length += 1`).
3. If we hit an invalid character (or the end of the string), the current contiguous 
   block ends. We calculate how many substrings can be formed from this block using 
   the formula: L * (L + 1) // 2, where L is the length of the block.
4. We add this to our `max_length` (total valid substrings) and reset `curr_length` to 0.
5. This reduces an $O(N^2)$ brute-force substring check down to a clean $O(N)$ linear pass.

Complexity Analysis:
- Time: O(N) per test case - Single pass through the string of length N.
- Space: O(K) where K is the number of valid characters stored in the set.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, k = map(int, input().split())
    s = input()
    # Using a set for O(1) character lookup
    valid_chars = set(input().split())

    curr_length = 0
    max_length = 0

    # Iterate through the string to find contiguous blocks of valid characters
    for r in range(n):
        if s[r] in valid_chars:
            curr_length += 1
        else:
            # Block broken: add combinations from the completed block
            max_length += (curr_length * (curr_length + 1)) // 2
            curr_length = 0

    # Add any remaining valid characters at the end of the string
    max_length += (curr_length * (curr_length + 1)) // 2
    
    print(max_length)

if __name__ == "__main__":
    solve()