"""
Day 17: Balanced Array (Codeforces 1343B)
Problem Link: https://codeforces.com/contest/1343/problem/B

Logic:
We need to construct an array of size N where the first half are distinct even 
numbers and the second half are distinct odd numbers, with both halves 
summing to the same value.
1. Parity Constraint: The sum of even numbers is always even. The sum of K 
   odd numbers is even ONLY if K is even. Since K = N/2, N must be divisible by 4.
2. Construction: 
   - First half: 2, 4, 6, ..., N
   - Second half: 1, 3, 5, ..., (N-3), and finally a number to balance the sum.
3. The last number = (Sum of Evens) - (Sum of first N/2-1 Odds).

Complexity Analysis:
- Time: O(N) - We iterate to build the halves.
- Space: O(N) - To store the constructed array.
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

        # Sum of N/2 even numbers is even. 
        # Sum of N/2 odd numbers is even only if N/2 is even.
        if (n // 2) % 2 != 0:
            print("NO")
        else:
            print("YES")
            arr = []
            sum_even = 0
            sum_odd = 0
            
            # Construct the even half
            for i in range(1, (n // 2 + 1)):
                val = 2 * i
                arr.append(val)
                sum_even += val
            
            # Construct the odd half (except the last element)
            for i in range(1, n // 2):
                val = 2 * i - 1
                arr.append(val)
                sum_odd += val

            # The last element must be odd and bridge the gap
            diff = sum_even - sum_odd
            arr.append(diff)

            print(*arr)

if __name__ == "__main__":
    solve()