"""
Day 37: Books (Codeforces 279B)
Problem Link: https://codeforces.com/contest/279/problem/B

Logic:
1. We use a sliding window [left, right] to find the maximum number 
   of books that can be read within time 't'.
2. The 'right' pointer expands the window by adding the time of the next book.
3. If the total time exceeds 't', the 'left' pointer contracts the window 
   from the start until the time is within the limit again.
4. The size of the window (right - left + 1) at each step gives a 
   valid number of books. We track the maximum size seen.

Complexity Analysis:
- Time: O(N) - Each pointer moves from 0 to N-1 exactly once.
- Space: O(N) - To store the array of book times.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: number of books, t: total time available
    line1 = input().split()
    if not line1: return
    n, t = map(int, line1)

    arr = list(map(int, input().split()))

    left = 0
    curr_time = 0
    max_books = 0

    # 'right' pointer explores every possible end-point
    for right in range(n):
        curr_time += arr[right]

        # Shrink the window from the left if we go over time
        while curr_time > t:
            curr_time -= arr[left]
            left += 1
            
        # The current valid window size is (right - left + 1)
        max_books = max(max_books, right - left + 1)     

    print(max_books)

if __name__ == "__main__":
    solve()