"""
Day 24: Similar Pairs (Codeforces 1360B)
Problem Link: https://codeforces.com/contest/1360/problem/C

Logic:
An even number n can be fully paired if:
1. The number of even elements and odd elements are both even.
2. OR, if there's at least one pair with a difference of 1, we can 
   remove that pair to flip the parity of the remaining counts.

Complexity Analysis:
- Time: O(N log N) due to sorting.
- Space: O(N) to store the array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    t = int(line1)

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        even = 0
        odd = 0
        for x in arr:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
        
        # If even count is already even, the odd count must also be even (since n is even)
        if even % 2 == 0:
            print("YES")
        else:
            # We need at least one pair with difference 1 to break the parity
            arr.sort()
            found = False
            for i in range(n - 1):
                if arr[i+1] - arr[i] == 1:
                    found = True
                    break
            
            if found:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()