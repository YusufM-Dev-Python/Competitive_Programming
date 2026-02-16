"""
Day 16: Odd/Even Increments (Codeforces 1669C)
Problem Link: https://codeforces.com/contest/1669/problem/C

Logic:
We can perform an operation: add 1 to all elements at even indices OR all 
elements at odd indices. 
- Adding 1 flips the parity (Even -> Odd, Odd -> Even).
- For the entire array to eventually have the same parity, all elements 
  at even positions must already share the same parity, and all elements 
  at odd positions must already share the same parity.

Complexity Analysis:
- Time: O(N) - We check each element once.
- Space: O(N) - To store the input array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        # Set the 'target' parity based on the first two elements
        tar_even = arr[0] % 2 
        tar_odd = arr[1] % 2
        
        possible = True
        
        # Check every element from index 2 onwards
        for i in range(2, n):
            if i % 2 == 0:
                # Even index must match parity of arr[0]
                if arr[i] % 2 != tar_even:
                    possible = False
                    break
            else:
                # Odd index must match parity of arr[1]
                if arr[i] % 2 != tar_odd:
                    possible = False
                    break
                    
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()