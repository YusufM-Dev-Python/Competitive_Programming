"""
Day 39: Raising Bacteria (Codeforces 579A)
Problem Link: https://codeforces.com/contest/579/problem/A

Logic:
1. Bacteria double every day (Power of 2).
2. To get 'x' bacteria, we look at the binary representation of x.
3. Each '1' in the binary form represents a day we had to manually 
   add a bacterium to the box.
4. Example: x = 5. Binary is 101. 
   - Add 1 (Day 0) -> 1
   - Wait (Day 1) -> 2
   - Wait (Day 2) -> 4
   - Add 1 (Day 2) -> 5. Total added: 2.

Complexity Analysis:
- Time: O(log X) - Number of bits in X.
- Space: O(1).
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line = input()
    if not line: return
    x = int(line)
    
    # Counting the set bits (1s) in binary
    count = 0
    while x > 0:
        if x % 2 != 0:
            count += 1
        x //= 2
        
    print(count)

    # Note: A one-liner alternative in Python:
    # print(bin(x).count('1'))

if __name__ == "__main__":
    solve()