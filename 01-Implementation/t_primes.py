"""
Day 33: T-primes (Codeforces 230B)
Problem Link: https://codeforces.com/contest/230/problem/B

Logic:
1. A number has exactly three divisors if it is a square of a prime number.
   Example: 4 (1, 2, 4), 9 (1, 3, 9), 25 (1, 5, 25).
2. The maximum input is 10^12, so we need to check primes up to sqrt(10^12) = 10^6.
3. We use the Sieve of Eratosthenes to find all primes up to 1,000,000.
4. For each query, check if it's a perfect square and if its root is prime.

Complexity Analysis:
- Time: O(M log log M + N) where M = 10^6 and N is the number of queries.
- Space: O(M) to store the prime boolean array.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read n
    line1 = input()
    if not line1: return
    n = int(line1)
    
    # Precompute Primes using Sieve of Eratosthenes up to 10^6
    limit = 1000000
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # Standard Sieve Optimization: Loop up to sqrt(limit)
    for i in range(2, 1001):
        if is_prime[i]:
            # Mark all multiples of i starting from i*i as False
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Read the numbers to check
    arr = list(map(int, input().split()))

    for num in arr:
        # Check if it's a perfect square
        root = int(num**0.5)
        
        # Verify: root*root must equal num and root must be prime
        if root * root == num and is_prime[root]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()