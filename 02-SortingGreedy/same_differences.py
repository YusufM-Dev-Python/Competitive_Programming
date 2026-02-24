"""
Day 23: Same Differences (Codeforces 1520D)
Problem Link: https://codeforces.com/contest/1520/problem/D

Logic:
The condition is a[j] - a[i] = j - i for i < j.
This can be rewritten as: a[j] - j = a[i] - i.
Let b[i] = a[i] - i. The problem becomes finding the number of pairs (i, j) 
such that b[i] = b[j].

1. Iterate through the array.
2. For each element, calculate val = arr[i] - i.
3. If 'val' has been seen K times before, it forms K new 'nice' pairs.
4. Update the frequency of 'val' in a hash map (dictionary).

Complexity Analysis:
- Time: O(N) - Single pass through the array.
- Space: O(N) - To store the frequency map in the worst case.
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
        arr = list(map(int, input().split()))
        
        count = 0
        # Frequency map to store occurrences of (arr[i] - i)
        mapi = {}

        for i in range(n):
            # Transform the condition into a frequency count problem
            val = arr[i] - i

            if val in mapi:
                # Every previous occurrence of 'val' forms a pair with this one
                count += mapi[val]
                mapi[val] += 1
            else:
                mapi[val] = 1
                
        print(count)

if __name__ == "__main__":
    solve()