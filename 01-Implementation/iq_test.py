"""
Day 34: IQ Test (Codeforces 25A)
Problem Link: https://codeforces.com/contest/25/problem/A

Logic:
1. We are given n numbers where all but one have the same parity (even/odd).
2. We need to find the 1-based index of the "outlier."
3. By storing the indices of even and odd numbers separately, we can 
   simply check which list has a length of 1.

Complexity Analysis:
- Time: O(N) - Single pass to categorize all numbers.
- Space: O(N) - To store the indices in lists.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    n = int(line1)
    
    arr = list(map(int, input().split()))

    evens = []
    odds = []

    # Categorize by index (0-based)
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    # The outlier is the one in the list with only one element
    # Convert to 1-based index for the output
    if len(evens) == 1:
        print(evens[0] + 1)
    else:
        print(odds[0] + 1)

if __name__ == "__main__":
    solve()