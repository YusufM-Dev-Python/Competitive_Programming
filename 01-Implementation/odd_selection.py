"""
Day 46: Odd Selection (Codeforces 1363A)
Problem Link: https://codeforces.com/contest/1363/problem/A

Logic:
1. An odd sum requires an odd number of odd elements.
2. Count total evens and odds.
3. Iterate through possible counts of odd elements (1, 3, 5...) that are <= x.
4. For each 'i' odds, we need 'x-i' evens. If we have enough of both, print "Yes".

Complexity Analysis:
- Time: O(N) per test case.
- Space: O(N) to store the array.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        # n: total elements, x: elements to pick
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        
        evens = 0
        odds = 0
        for num in arr:
            if num % 2 == 0:
                evens += 1
            else:
                odds += 1
                
        possible = False

        # 'i' represents the number of odd elements we pick
        # It must be odd: 1, 3, 5...
        for i in range(1, odds + 1, 2):
            if i <= x:
                needed_evens = x - i
                if needed_evens <= evens:
                    possible = True
                    break
                
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()