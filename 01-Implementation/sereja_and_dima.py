"""
Day 17: Sereja and Dima (Codeforces 381A)
Problem Link: https://codeforces.com/contest/381/problem/A

Logic:
This is a Two Pointers simulation of a greedy game.
1. Two players (Sereja and Dima) take turns picking the largest card 
   available at either the leftmost (l) or rightmost (r) end of the row.
2. Sereja always goes first (even turns: 0, 2, 4...).
3. By comparing arr[l] and arr[r], we determine which card is taken 
   and increment the respective player's score.

Complexity Analysis:
- Time: O(N) - We traverse the array exactly once with two pointers.
- Space: O(N) - To store the initial array of cards.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n_input = input()
    if not n_input: return
    n = int(n_input)
    
    arr = list(map(int, input().split()))

    l = 0
    r = n - 1
    turn = 0
    sereja_s = 0
    dima_s = 0

    # Continue until the pointers meet and all cards are taken
    while l <= r:
        # Optimal move: pick the larger value between the two ends
        if arr[l] > arr[r]:
            choose = arr[l]
            l += 1
        else:
            choose = arr[r]
            r -= 1
        
        # Alternate scoring: Sereja takes even turns, Dima takes odd
        if turn % 2 == 0:
            sereja_s += choose
        else:
            dima_s += choose
        
        turn += 1

    print(sereja_s, dima_s)

if __name__ == "__main__":
    solve()