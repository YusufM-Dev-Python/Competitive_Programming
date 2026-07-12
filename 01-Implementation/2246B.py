"""
Day 99: Construction (Codeforces 2246B)
Topic: Implementation / Construction
Logic:
1. Handle base cases for small n: n=1 prints 1, n=2 is impossible (-1).
2. For n >= 3, construct a sequence starting with [1, 2, 3].
3. For subsequent elements, append the previous value multiplied by 2 to satisfy 
   the problem's specific construction constraints.
4. This approach ensures each element follows the growth pattern required by the contest problem.

Complexity Analysis:
- Time: O(N) - We iterate from 3 to n to fill the array.
- Space: O(N) - To store the sequence of length n.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())

        if n == 1:
            print(1)
        elif n == 2:
            print(-1)
        else:
            arr = [1, 2, 3]
            # Build the sequence using the doubling pattern
            for i in range(3, n):
                arr.append(arr[i-1] * 2)
            print(*arr)

if __name__ == "__main__":
    solve()