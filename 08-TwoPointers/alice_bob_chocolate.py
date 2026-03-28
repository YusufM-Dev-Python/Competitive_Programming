"""
Day 42: Alice, Bob and Chocolate (Codeforces 6C)
Problem Link: https://codeforces.com/contest/6/problem/C

Logic:
1. Alice starts at index 0, Bob at index n-1.
2. We track the total time each has spent eating.
3. If Alice's total time <= Bob's total time, Alice eats the next 
   available chocolate (moving 'l' forward).
4. Otherwise, Bob eats the next one (moving 'r' backward).
5. The loop continues until all chocolates are eaten (l > r).

Complexity Analysis:
- Time: O(N) - Single pass through the chocolates.
- Space: O(N) - To store the chocolate eating times.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    n = int(line1)
    
    # Eating times for each chocolate
    arr = list(map(int, input().split()))

    l = 0
    r = n - 1

    time_alice = 0
    time_bob = 0

    # Two-pointer competition simulation
    while l <= r:
        # Alice gets priority if times are equal
        if time_alice <= time_bob:
            time_alice += arr[l]
            l += 1
        else:
            time_bob += arr[r]
            r -= 1
            
    # After the loop, 'l' is the number of chocolates Alice ate
    # 'n - l' is the number of chocolates Bob ate
    print(f"{l} {n - l}")
    
if __name__ == "__main__":
    solve()