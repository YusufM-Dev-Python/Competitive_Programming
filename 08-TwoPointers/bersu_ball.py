"""
Day 45: Bersu Ball (Codeforces 489B)
Problem Link: https://codeforces.com/contest/489/problem/B

Logic:
1. To maximize pairs, sort both boys' and girls' skill levels.
2. Use two pointers (b and g) to iterate through the lists.
3. If the skill difference is <= 1, they can dance together. Increment pairs and move both.
4. If the difference is > 1, increment the pointer of the person with the LOWER skill,
   as they have no hope of matching with anyone else in the other sorted list.

Complexity Analysis:
- Time: O(N log N + M log M) - Due to sorting both arrays.
- Space: O(N + M) - To store the skill levels.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read boys' data
    line1 = input()
    if not line1: return
    n = int(line1)
    boys = list(map(int, input().split()))
    
    # Read girls' data
    line3 = input()
    if not line3: return
    m = int(line3)
    girls = list(map(int, input().split()))

    # Sorting is the key to the greedy approach
    boys.sort()
    girls.sort()

    b = 0
    g = 0
    pairs = 0

    # Two-pointer matching
    while b < n and g < m:
        if abs(boys[b] - girls[g]) <= 1:
            # Found a valid pair
            pairs += 1
            b += 1
            g += 1
        elif boys[b] < girls[g]:
            # Boy is too unskilled for the current girl (and all girls after her)
            b += 1
        else:
            # Girl is too unskilled for the current boy (and all boys after him)
            g += 1
            
    print(pairs)

if __name__ == "__main__":
    solve()