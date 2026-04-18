"""
Day 60 Milestone: Team Formation (Codeforces Style Greedy)
Logic:
1. Sort players in descending order (strongest first).
2. Use a two-pointer approach (l=0, r=n-1).
3. For the strongest available player at 'l', calculate how many 
   total players are needed to make a team > D.
4. If we have enough players left (including the weak ones at 'r'),
   form the team, increment count, and move 'r' to sacrifice the weakest.
5. If we can't form a team, we're done.

Complexity Analysis:
- Time: O(N log N) for sorting.
- Space: O(1) beyond input storage.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n = number of players, d = defense value to beat
    line = input().split()
    if not line: return
    n, d = map(int, line)
    p = list(map(int, input().split()))

    # Sort strongest to weakest
    p.sort(reverse=True)

    l = 0
    r = n - 1
    teams = 0
    
    while l <= r:
        # Number of players needed for a team led by p[l]
        # to have total power > d
        needed_count = (d // p[l]) + 1

        # (r - l + 1) is the number of players currently available
        if (r - l + 1) >= needed_count:
            teams += 1
            l += 1
            # Use up the 'needed_count - 1' weakest players
            r -= (needed_count - 1)
        else:
            # Not enough players left to form another valid team
            break
        
    print(teams)

if __name__ == "__main__":
    solve()