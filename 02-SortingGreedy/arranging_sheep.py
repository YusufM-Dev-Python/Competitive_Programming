"""
Day 53: Arranging The Sheep (Codeforces 1520E)
Logic:
1. To minimize moves, the sheep should cluster around the median sheep.
2. The distance to the median is adjusted by the sheep's relative 
   position to account for the space they occupy in the final line.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        s = input()

        # Find all sheep positions
        sheep = [i for i, char in enumerate(s) if char == "*"]

        if not sheep:
            print(0)
            continue

        # Target the median sheep as the anchor
        anchor_idx = len(sheep) // 2
        anchor_pos = sheep[anchor_idx]

        total_moves = 0
        for i in range(len(sheep)):
            # Moves = |CurrentPos - TargetPos| - |CurrentIndex - TargetIndex|
            total_moves += abs(sheep[i] - anchor_pos) - abs(i - anchor_idx)
            
        print(total_moves)

if __name__ == "__main__":
    solve()