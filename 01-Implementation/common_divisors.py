"""
Day 30: Common Divisors (Codeforces 1203C)
Problem Link: https://codeforces.com/contest/1203/problem/C

Logic:
1. The common divisors of all numbers in an array are the divisors of their GCD.
2. First, calculate the GCD of the entire array.
3. Then, count the divisors of that GCD in O(sqrt(GCD)) time.
4. For every i that divides GCD, if i*i != GCD, we count two divisors (i and GCD/i).

Complexity Analysis:
- Time: O(N + sqrt(GCD)) - GCD computation takes O(N * log(max_A)), 
  and divisor counting takes O(sqrt(GCD)).
- Space: O(N) to store the input array.
"""

import sys
import math

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    n = int(line1)
    arr = list(map(int, input().split()))
    
    # Calculate the GCD of all numbers in the array
    current_gcd = arr[0]
    for i in range(1, n):
        current_gcd = math.gcd(current_gcd, arr[i])
    
    count = 0
    i = 1
    # Standard O(sqrt(N)) divisor counting
    while i * i <= current_gcd:
        if current_gcd % i == 0:
            if i * i == current_gcd:
                count += 1 # Perfect square case
            else:
                count += 2 # Pair of divisors (i and current_gcd // i)
        i += 1
        
    print(count)

if __name__ == "__main__":
    solve()