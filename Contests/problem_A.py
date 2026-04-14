"""
Day 56: Contest Problem A
Logic:
1. To satisfy the problem's condition (likely avoiding adjacent duplicates 
   or creating a specific sequence), we sort the array in reverse.
2. If any two adjacent elements are equal after sorting, it means we 
   cannot satisfy the condition with the given elements.
3. Output -1 if impossible, otherwise output the sorted array.

Complexity Analysis:
- Time: O(N log N) due to sorting.
- Space: O(N) to store the input array.
"""

import sys

# Faster I/O for contest pressure
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n_str = input()
        if not n_str: continue
        n = int(n_str)
        arr = list(map(int, input().split()))

        # Reverse sorting is a common strategy to satisfy 
        # prefix sum or adjacency constraints in 'A' problems.
        arr.sort(reverse=True)

        flag = False
        # Check for adjacent duplicates
        for i in range(1, n):
            if arr[i-1] == arr[i]:
                flag = True
                break

        if flag:
            print(-1)
        else:
            print(*arr)

if __name__ == "__main__":
    solve()