"""
Day 70: Restoring Three Numbers (Codeforces 1154A)
Logic:
1. The input contains a+b, a+c, b+c, and a+b+c.
2. The largest number is always a+b+c.
3. Subtract the other three numbers from the largest to find a, b, and c.

Complexity Analysis:
- Time: O(1) - Sorting 4 elements is constant time.
- Space: O(1) - Storing 4 elements.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read the 4 numbers
    line = input()
    if not line: return
    arr = list(map(int, line.split()))
    
    # Sort to find the largest (which is a + b + c)
    arr.sort()
    
    # Total sum is the last element
    abc = arr[3]
    
    # The three numbers are the differences
    a = abc - arr[0]
    b = abc - arr[1]
    c = abc - arr[2]
    
    print(f"{a} {b} {c}")

if __name__ == "__main__":
    solve()