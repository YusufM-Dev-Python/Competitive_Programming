"""
Day 13: Doremy's Paint 3 (Codeforces 1890A)
Problem Link: https://codeforces.com/contest/1890/problem/A

Logic:
To make all adjacent sums equal, we need the array to alternate between two 
numbers (e.g., a, b, a, b...). This is only possible if:
1. There are at most 2 distinct numbers in the array.
2. The frequency of these two numbers is as balanced as possible.
   For an array of length N, the counts must be (N//2) and (N - N//2).
   Using abs(c1 - c2) <= 1 handles both even and odd N perfectly.

Complexity Analysis:
- Time: O(N) to count frequencies using Counter.
- Space: O(N) to store the input array.
"""

from collections import Counter
import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        # Frequency map of all elements
        counts = Counter(arr)

        # Condition 1: More than 2 distinct numbers cannot alternate 
        # to produce equal adjacent sums.
        if len(counts) > 2:
            print("NO")
        
        # Condition 2: If only 1 distinct number, all sums are naturally equal.
        elif len(counts) == 1:
            print("YES")
        
        # Condition 3: If 2 distinct numbers, their counts must be balanced.
        else:
            c1, c2 = counts.values()
            # In an alternating sequence, the counts can differ by at most 1.
            if abs(c1 - c2) <= 1:
                print("YES")
            else:
                print("NO")
    
if __name__ == "__main__":
    solve()