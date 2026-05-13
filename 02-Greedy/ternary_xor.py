"""
Day 25: Ternary XOR (Codeforces 1325B)
Problem Link: https://codeforces.com/contest/1325/problem/C

Logic:
We want to minimize max(a, b) where a ⊕ b = x (ternary XOR).
- As long as a and b are equal, we split '2' into (1, 1) and '0' into (0, 0).
- The first '1' we encounter must be split into (1, 0). Now a > b.
- For all characters after this point, to keep 'a' small, we give everything to 'b'.
- This means for any digit 'd' after the first '1', a gets '0' and b gets 'd'.

Complexity Analysis:
- Time: O(N) - Single pass through the string of length N.
- Space: O(N) - To store the resulting strings a and b.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        x = input()

        a = []
        b = []
        # 'tie' tracks if one number has already become strictly greater than the other
        already_greater = False

        for char in x:
            if not already_greater:
                if char == '2':
                    # Keep them balanced
                    a.append('1')
                    b.append('1')
                elif char == '0':
                    a.append('0')
                    b.append('0')
                elif char == '1':
                    # First difference: a becomes greater than b
                    a.append('1')
                    b.append('0')
                    already_greater = True
            else:
                # 'a' is already larger, so give all weight to 'b' to minimize 'a'
                a.append('0')
                b.append(char)

        print("".join(a))
        print("".join(b))
        
if __name__ == "__main__":
    solve()