"""
Day 77: Dragons (Codeforces 230A)
Topic: Greedy / Sorting
Logic:
1. To maximize the chances of defeating all dragons, Kirito should always fight 
   the weakest dragon currently available to gain bonus strength.
2. We store the dragons as tuples of (strength, bonus) and sort them by strength.
3. We iterate through the sorted list:
   - If Kirito's current strength 's' is less than or equal to the dragon's strength, 
     he cannot defeat it, so we print "NO".
   - Otherwise, he defeats it and gains the bonus 'y'.
4. If he successfully defeats all dragons, we print "YES".

Complexity Analysis:
- Time: O(N log N) - Due to sorting the array of dragons.
- Space: O(N) - Storing the dragon data in a list.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    s, n = map(int, input().split())
    dragons = []
    for _ in range(n):
        x, y = map(int, input().split())
        dragons.append((x, y))

    # Sort dragons greedily by their strength (x)
    dragons.sort(key=lambda d: d[0])
    
    for i, j in dragons:
        if s <= i:
            print("NO")
            return
        s += j

    print("YES")

if __name__ == "__main__":
    solve()