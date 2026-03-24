"""
Day 38: Ternary String (Codeforces 1354B)
Problem Link: https://codeforces.com/contest/1354/problem/B

Logic:
1. Use a sliding window [left, right] to find the shortest substring 
   containing characters '1', '2', and '3'.
2. Expand 'right' to include new characters and update their frequency.
3. While all three characters are present (freq >= 1):
   - Update the global minimum length (right - left + 1).
   - Try to remove the character at 'left' to see if a smaller 
     valid substring exists.
4. If min_len remains infinity, no valid substring was found (print 0).

Complexity Analysis:
- Time: O(N) - Each character is visited by 'left' and 'right' pointers once.
- Space: O(1) - The frequency dictionary only ever holds 3 keys.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        s = input()
        # Frequency map for our three target characters
        freq = {'1': 0, '2': 0, '3': 0}
        min_len = float('inf')
        left = 0
        
        for right in range(len(s)):
            # Add the current character to the window
            freq[s[right]] += 1

            # While the window contains all required characters, shrink it
            while freq['1'] >= 1 and freq['2'] >= 1 and freq['3'] >= 1:
                # Update our best result
                min_len = min(min_len, right - left + 1)
                
                # Try to shorten from the left
                freq[s[left]] -= 1
                left += 1
                
        # Handle the case where no valid substring exists
        if min_len == float('inf'):
            print(0)
        else:
            print(min_len)

if __name__ == "__main__":
    solve()