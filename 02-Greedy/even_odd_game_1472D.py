"""
Day 68: Even-Odd Game (Codeforces 1472D)
Logic:
1. Standard greedy game theory: Both players always pick the largest remaining number.
2. Sorting the array once in descending order allows O(1) turn processing.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # The key to 1472D: Sorting descending
        arr.sort(reverse=True)
        
        alice = 0
        bob = 0
        
        for i in range(n):
            if i % 2 == 0: # Alice's turn
                if arr[i] % 2 == 0:
                    alice += arr[i]
            else: # Bob's turn
                if arr[i] % 2 != 0:
                    bob += arr[i]
                    
        if alice > bob:
            print("Alice")
        elif bob > alice:
            print("Bob")
        else:
            print("Tie")

if __name__ == "__main__":
    solve()