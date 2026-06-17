"""
Day 81: Increasing (Codeforces 1742B)
Topic: Greedy / Sorting / Data Structures
Logic:
1. An array can be rearranged into a strictly increasing sequence if and only if 
   all its elements are distinct.
2. If there are any duplicate elements, they can never be placed such that a[i] < a[i+1].
3. We utilize a Python set to filter out duplicate elements from the array.
4. If the size of the set matches the original array length 'n', it means all elements 
   are unique, so we output "YES". Otherwise, we output "NO".

Complexity Analysis:
- Time: O(N) - Creating a set from the array takes linear time on average.
- Space: O(N) - Storing unique elements within the set structure.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # A strictly increasing array cannot contain duplicate values
        if len(set(arr)) == n:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()