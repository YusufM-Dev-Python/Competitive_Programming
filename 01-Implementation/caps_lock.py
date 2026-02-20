"""
Day 20: cAPS lOCK (Codeforces 131A)
Problem Link: https://codeforces.com/contest/131/problem/A

Logic:
Caps Lock is considered accidentally on if:
1. All letters are uppercase (e.g., "CAPS").
2. Only the first letter is lowercase and the rest are uppercase (e.g., "cAPS").

In both cases, we must swap the case of all letters. Otherwise, we leave 
the word exactly as it is.

Complexity Analysis:
- Time: O(N) where N is the length of the string.
- Space: O(N) to store and return the transformed string.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    s = input()
    if not s: return

    # Case 1: All letters are uppercase
    condition1 = s.isupper()
    
    # Case 2: First letter is lowercase, and all following letters are uppercase
    # Note: s[1:].isupper() is True for strings of length 1
    condition2 = s[0].islower() and (len(s) == 1 or s[1:].isupper())

    if condition1 or condition2:
        # Swap the case of all characters
        print(s.swapcase())
    else:
        # Print the original string as is
        print(s)
    
if __name__ == "__main__":
    solve()