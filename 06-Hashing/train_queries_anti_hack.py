"""
Day 51: Train and Queries (Codeforces 1702C)
Logic:
1. For each station, store its FIRST occurrence and its LAST occurrence.
2. For a query (a, b), a path exists if station 'a' appears before 'b' disappears.
3. Anti-Hack: Use a random XOR shield for dictionary keys to prevent 
   engineered hash collisions that cause TLE in Python.

Complexity:
- Time: O(N + K) - Linear scan to build the map, then O(1) per query.
- Space: O(N) - To store station indices.
"""

import sys
import random

# Anti-hash-collision shield
Random = random.getrandbits(64)
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        # Handle the blank line between test cases in 1702C
        try:
            input() 
            line = input().split()
            if not line: break
            n, k = map(int, line)
            arr = list(map(int, input().split()))
        except EOFError:
            break
    
        # Store [first_occurrence, last_occurrence]
        mappi = {}
        for i in range(n):
            # Apply XOR shield to the key
            station = arr[i] ^ Random
            if station not in mappi:
                mappi[station] = [i, i]
            else:
                mappi[station][1] = i

        ans = []
        for _ in range(k):
            try:
                a, b = map(int, input().split())
                a_shield = a ^ Random
                b_shield = b ^ Random

                if a_shield not in mappi or b_shield not in mappi:
                    ans.append("NO")
                elif mappi[a_shield][0] <= mappi[b_shield][1]:
                    ans.append("YES")
                else:
                    ans.append("NO")
            except ValueError:
                break

        print('\n'.join(ans))

if __name__ == '__main__':
    solve()