"""
Day 43: Exams (Codeforces 479C)
Problem Link: https://codeforces.com/contest/479/problem/C

Logic:
1. We want to finish all exams as early as possible.
2. Sort the exams primarily by their scheduled date (a).
3. For each exam, we have two options: the early date (b) or the scheduled date (a).
4. If the early date 'b' is >= the day we finished the previous exam, 
   we take the exam on day 'b' to keep the schedule as early as possible.
5. Otherwise, we must take it on day 'a'.

Complexity Analysis:
- Time: O(N log N) - Due to sorting the list of exams.
- Space: O(N) - To store the list of n exams.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    n = int(line1)
    
    exams = []
    for _ in range(n):
        # a is the scheduled date, b is the early date
        a, b = map(int, input().split())
        exams.append((a, b))
    
    # Sort by 'a' primarily, then by 'b'
    exams.sort()

    curr_day = 0
    for a, b in exams:
        # Try to take the exam on the earlier date 'b'
        if b >= curr_day:
            curr_day = b
        else:
            # If 'b' is too early, we are forced to use date 'a'
            curr_day = a
            
    print(curr_day)

if __name__ == "__main__":
    solve()