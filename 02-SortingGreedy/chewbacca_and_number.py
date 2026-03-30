"""
Day 44: Chewbacca and Number (Codeforces 514A)
Problem Link: https://codeforces.com/contest/514/problem/A

Logic:
1. For each digit 'd', we can replace it with '9-d'.
2. To minimize the number, we choose min(d, 9-d) for each position.
3. Exception: The first digit cannot be 0. So if the first digit is 9, 
   we keep it as 9 (since 9-9=0).

Complexity Analysis:
- Time: O(L) where L is the number of digits in x.
- Space: O(L) to store the character array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    x = input().strip()
    if not x: return
    arr = list(x)

    for i in range(len(arr)):
        d = int(arr[i])
        inverted = 9 - d

        # Rule 1: We want the smaller of d and inverted
        if inverted < d:
            # Rule 2: Don't allow a leading zero
            if i == 0 and inverted == 0:
                continue
            arr[i] = str(inverted)
            
    print("".join(arr))

if __name__ == '__main__':
    solve()