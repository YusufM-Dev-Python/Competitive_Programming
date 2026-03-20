"""
Day 34: Pashmak and Flowers (Codeforces 459B)
Problem Link: https://codeforces.com/contest/459/problem/B

Logic:
1. Max difference is simply max(arr) - min(arr).
2. To count the ways:
   - If max_val != min_val: Ways = (count of min_val) * (count of max_val).
   - If max_val == min_val: All flowers are the same. Ways = n * (n-1) // 2.

Complexity Analysis:
- Time: O(N) - We traverse the array to find min, max, and their counts.
- Space: O(N) - To store the array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    n = int(line1)
    
    arr = list(map(int, input().split()))

    max_val = max(arr)
    min_val = min(arr)

    max_diff = max_val - min_val

    # Case: All elements are the same
    if max_val == min_val:
        # Combinations of n items taken 2 at a time: nC2
        ways = n * (n - 1) // 2
        print(f"{max_diff} {ways}")
    else:
        # Case: Distinct max and min values
        count_max = arr.count(max_val)
        count_min = arr.count(min_val)
        print(f"{max_diff} {count_max * count_min}")

if __name__ == "__main__":
    solve()