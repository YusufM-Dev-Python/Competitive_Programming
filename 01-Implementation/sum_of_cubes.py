"""
Day 28: Sum of Cubes (Codeforces 1490C)
Problem Link: https://codeforces.com/contest/1490/problem/C

Logic:
Check if x can be represented as a^3 + b^3 where a, b >= 1.
1. Iterate 'a' from 1 up to x^(1/3).
2. Calculate the remaining value: tar = x - a^3.
3. If tar > 0 and tar is a perfect cube, output YES.
4. To check if 'tar' is a perfect cube, take its cube root, round it, 
   and see if its cube equals 'tar'.

Complexity Analysis:
- Time: O(T * x^(1/3)) - Approximately 10,000 iterations per test case.
- Space: O(1).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line = input()
    if not line: return
    t = int(line)

    for _ in range(t):
        x = int(input())
        found = False
        i = 1
        
        # Iterate through possible values of 'a'
        # i*i*i < x ensures 'tar' will be at least 1
        while i * i * i < x:
            tar = x - (i * i * i)
            
            # Check if the remainder is a perfect cube
            b = round(tar**(1/3))
            
            # Re-verify to avoid floating point precision issues
            if (b * b * b) == tar:
                print("YES")
                found = True
                break
            i += 1
            
        if not found:
            print("NO")
    
if __name__ == "__main__":
    solve()