"""
Day 15: Cypher (Codeforces 1703C)
Problem Link: https://codeforces.com/contest/1703/problem/C

Logic:
We are given the final state of a combination lock and a sequence of moves 
(Up/Down). To find the original state, we reverse every move:
- A 'Down' (D) move means the original digit was one higher (+1).
- An 'Up' (U) move means the original digit was one lower (-1).
Since the digits are circular (0-9), we use modulo 10 to wrap around.

Complexity Analysis:
- Time: O(N * L) where N is the number of wheels and L is the number of moves.
- Space: O(N) to store the state of the wheels.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input()) # Number of wheels
        arr = list(map(int, input().split())) # Final state of wheels
        
        for i in range(n):
            line = input().split()
            # num = int(line[0]) -> Number of moves (not used in calculation)
            moves = line[1]

            for char in moves:
                if char == 'D':
                    # Reverse 'Down' by moving the digit 'Up'
                    arr[i] = (arr[i] + 1) % 10
                else:
                    # Reverse 'Up' by moving the digit 'Down'
                    # Adding 10 before modulo handles negative results in Python
                    arr[i] = (arr[i] - 1 + 10) % 10
                    
        # Print the reconstructed original combination
        print(*arr)

if __name__ == "__main__":
    solve()