"""
Day 32: Registration System (Codeforces 4C)
Problem Link: https://codeforces.com/contest/4/problem/C

Logic:
1. We need to store names and their occurrence counts.
2. For each new name:
   - If it's the first time we see it, store it and print "OK".
   - If it exists, append its current count to the name, print the new name,
     and increment the original name's counter in the map.

Complexity Analysis:
- Time: O(N * L) - where N is number of names and L is average length of a name.
- Space: O(N * L) - to store all unique names in the dictionary.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    n = int(t_str)
    
    # Dictionary to keep track of name frequencies
    db = {}
    
    for _ in range(n):
        s = input()
        
        if s not in db:
            # First time seeing this name
            db[s] = 1
            print("OK")
        else:
            # Name exists, generate the new unique version
            count = db[s]
            new_name = s + str(count)
            print(new_name)
            
            # Increment the count for the base name
            db[s] += 1
            
            # Note: We don't strictly need to add the new_name to db 
            # because the problem guarantees new_name won't be requested 
            # by the system itself, but adding it doesn't hurt.

if __name__ == "__main__":
    solve()