"""
Day 99 (Part 2): 1932B - Seating Arrangements / Milestones
Topic: Greedy / Math
Logic:
1. The problem requires us to find a strictly increasing sequence of values, 
   where the i-th value is a multiple of the input array's i-th element.
2. Starting from a baseline of 0, for each element 'a', we calculate the smallest 
   multiple of 'a' that is strictly greater than the current 'year' (milestone).
3. The formula (current_year // a + 1) * a efficiently jumps to the next 
   valid multiple in O(1) time.

Complexity Analysis:
- Time: O(N) per test case - Single pass through the input array.
- Space: O(1) - Minimal extra space beyond input storage.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        current_year = 0
        for a in arr:
            # Smallest multiple of 'a' strictly greater than current_year
            current_year = (current_year // a + 1) * a
            
        print(current_year)

if __name__ == '__main__':
    solve()