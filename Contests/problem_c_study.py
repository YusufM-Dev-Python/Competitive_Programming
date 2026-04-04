"""
Day 47: Codeforces Round 1090 (Div. 4) - Problem C (Study)
Problem Link: (Pending Official Name/Link)

Logic (Construction):
1. The goal is to construct an array of 3n elements using numbers from 1 to 3n.
2. We use a "Two-Pointer" style construction.
3. We pick the smallest available number (1, 2, 3...) and the 
   two largest available numbers (3n, 3n-1...).
4. This grouping often helps in maintaining a specific property 
   (like sum or divisibility) across the triplets.

Complexity Analysis:
- Time: O(N) per test case to build the array.
- Space: O(N) to store the result.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n_str = input()
        if not n_str: continue
        n = int(n_str)

        arr = []
        small = 1
        large = 3 * n

        # Build n triplets
        for _ in range(n):
            # Construction: [Smallest, Largest-1, Largest]
            arr.append(small)
            arr.append(large - 1)
            arr.append(large)

            # Move pointers inward
            small += 1
            large -= 2
        
        # Unpack list into space-separated integers
        print(*arr)

if __name__ == "__main__":
    solve()