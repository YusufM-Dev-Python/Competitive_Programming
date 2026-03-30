"""
Day 44: Given Length and Sum of Digits... (Codeforces 489C)
Problem Link: https://codeforces.com/contest/489/problem/C

Logic:
1. Max Number: Fill slots from left to right with '9's until sum is exhausted.
2. Min Number: 
   - Start by putting '1' in the first slot (to avoid leading zero).
   - Fill slots from RIGHT to LEFT with '9's to keep the front digits small.
   - Add the remaining sum back to the first slot.
3. Special Case: m=1, s=0 is "0 0". Otherwise, s=0 with m>1 is impossible.

Complexity Analysis:
- Time: O(M) - Linear passes to fill the digit lists.
- Space: O(M) - To store the strings of length M.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    m, s = map(int, input().split())

    # Handle impossible cases
    # m > 1 and s == 0 means "00..." which isn't allowed.
    # s > 9*m means even all 9s won't reach the sum.
    if (s == 0 and m > 1) or (s > 9 * m):
        print("-1 -1")
        return
    
    # Handle the specific case for 0
    if s == 0 and m == 1:
        print("0 0")
        return

    # MAX NUMBER: Greedy Left to Right
    max_num = ['0'] * m
    temp_s = s
    for i in range(m):
        can_add = min(9, temp_s)
        max_num[i] = str(can_add)
        temp_s -= can_add

    # MIN NUMBER: Greedy Right to Left (saving 1 for the front)
    min_num = ['0'] * m
    min_num[0] = '1'
    temp_s = s - 1 # Use 1 for the first digit

    for i in range(m - 1, 0, -1):
        can_add = min(9, temp_s)
        min_num[i] = str(can_add)
        temp_s -= can_add
    
    # Add whatever is left from our 'budget' to the first digit
    min_num[0] = str(int(min_num[0]) + temp_s)

    print(f"{''.join(min_num)} {''.join(max_num)}")

if __name__ == "__main__":
    solve()