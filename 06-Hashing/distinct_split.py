"""
Day 59: Distinct Split (Codeforces 1791D)
Logic:
1. We need to split string S into two non-empty strings a and b such that 
   f(a) + f(b) is maximized (where f is the number of distinct characters).
2. We use a frequency map for the right side and a set for the left side.
3. As we iterate through the string, we "move" the character from the 
   right frequency map to the left set.
4. Update the distinct counts in O(1) at each step and track the maximum.

Complexity Analysis:
- Time: O(N) - Linear scan across the string.
- Space: O(1) - The maps/sets only ever store up to 26 characters (lowercase Latin).
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        s = input()

        # Step 1: Initial state - everything is in the 'right' part
        right_m = {}
        for char in s:
            right_m[char] = right_m.get(char, 0) + 1
            
        right_distinct_count = len(right_m)
        left_m = set()
        max_score = 0

        # Step 2: Iterate through the split points
        # We don't need to check the last character split because parts must be non-empty
        for i in range(n - 1):
            char = s[i]
            # Move character to the 'left' set
            left_m.add(char)
            
            # Remove character from the 'right' frequency map
            right_m[char] -= 1
            if right_m[char] == 0:
                right_distinct_count -= 1
            
            # Score = (Distinct in Left) + (Distinct in Right)
            current_score = len(left_m) + right_distinct_count
            if current_score > max_score:
                max_score = current_score
            
        print(max_score)

if __name__ == "__main__":
    solve()