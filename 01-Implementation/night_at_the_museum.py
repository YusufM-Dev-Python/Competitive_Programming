"""
Day 71: Night at the Museum (Codeforces 731A)
Logic:
1. The alphabet wheel is circular (26 letters).
2. For any two letters, there are two ways to move: clockwise or counter-clockwise.
3. Distance d = |ord(char1) - ord(char2)|.
4. Minimal distance = min(d, 26 - d).
5. Accumulate this distance for each character in the string, starting from 'a'.

Complexity Analysis:
- Time: O(N) where N is the length of the string.
- Space: O(1) beyond storing the input string.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    s = input()
    if not s: return
    
    curr = 'a'
    total_time = 0
    
    for char in s:
        # Straight-line distance in the alphabet
        d = abs(ord(curr) - ord(char))
        
        # Minimum of going forward or wrapping around the circle
        total_time += min(d, 26 - d)
        
        # Update current position to the letter just "printed"
        curr = char
        
    print(total_time)

if __name__ == "__main__":
    solve()