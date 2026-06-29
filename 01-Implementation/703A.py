"""
Day 87: Mishka and Game (Codeforces 703A)
Topic: Implementation / Simulation
Logic:
1. We simulate 'n' rounds of a game played by Mishka and Chris.
2. For each round, we compare their respective dice rolls (m and c).
   - If m > c, Mishka wins the round.
   - If c > m, Chris wins the round.
   - If m == c, nobody gets a point.
3. After all rounds, we compare the total wins to announce the final outcome: "Mishka", "Chris", or a tie.

Complexity Analysis:
- Time: O(N) - We iterate exactly through the 'n' rounds.
- Space: O(1) - Only a few primitive integer counters are used.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    miski = 0
    chris = 0
    for _ in range(n):
        m, c = map(int, input().split())

        if m > c:
            miski += 1
        if c > m:
            chris += 1
        
    if chris > miski:
        print("Chris")
    elif miski > chris:
        print("Mishka")
    else:
        print("Friendship is magic!^^")

if __name__ == "__main__":
    solve()