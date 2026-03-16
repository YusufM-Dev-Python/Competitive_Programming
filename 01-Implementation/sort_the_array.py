"""
Day 32: Sort the Array (Codeforces 451B)
Problem Link: https://codeforces.com/contest/451/problem/B

Logic:
1. We can reverse exactly one segment to make the array sorted.
2. To find this segment, compare the array with its sorted version.
3. The first mismatch from the left is our start 'L', and the first 
   mismatch from the right is our end 'R'.
4. Reverse the segment [L, R] and check if the result is sorted.

Complexity Analysis:
- Time: O(N log N) - Due to the initial sorting. The rest is O(N).
- Space: O(N) - To store the sorted copy of the array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    n = int(line1)
    arr = list(map(int, input().split()))
    
    # Create a sorted reference
    sorted_arr = sorted(arr)

    # Find the first mismatch from the left
    l = 0
    while l < n and arr[l] == sorted_arr[l]:
        l += 1

    # Case: Already sorted
    if l == n:
        print("yes")
        print("1 1")
        return
    
    # Find the first mismatch from the right
    r = n - 1
    while r >= 0 and arr[r] == sorted_arr[r]:
        r -= 1
    
    # Reverse the segment in-place
    # Python slice assignment makes this very clean
    arr[l:r+1] = reversed(arr[l:r+1])

    # Verify if one flip was enough
    if arr == sorted_arr:
        print("yes")
        print(f"{l+1} {r+1}") # Output 1-based indices
    else:
        print("no")
        
if __name__ == "__main__":
    solve()