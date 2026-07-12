"""
Day 99: Construction (Codeforces 2246A)
Topic: Implementation / Construction
Logic:
1. The goal is to construct a sequence based on the input size 'n'.
2. By iterating from 'n' down to 1 and placing each value into the array at indices 
   0 to n-1, we generate a descending permutation.
3. This is a classic construction pattern often used in introductory contest problems.

Complexity Analysis:
- Time: O(N) - We perform a single pass to fill the array.
- Space: O(N) - To store the generated sequence.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        
        # Construct the sequence
        arr = [0] * n
        for i in range(n, 0, -1):
            arr[n - i] = i
        
        # Unpack the list for clean output
        print(*arr)

if __name__ == '__main__':
    solve()