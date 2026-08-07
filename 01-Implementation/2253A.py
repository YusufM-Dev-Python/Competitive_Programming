"""
Day 122: 2253A - Contest Primality Testing
Topic: Number Theory / Math
Goal: Determine whether 'n + 1' is a prime number for each test case.

Logic:
1. Candidate Value: Set `a = n + 1`.
2. Primality Check: 
   - Numbers less than 2 are not prime.
   - For numbers $\ge 2$, check divisibility from `i = 2` up to $\sqrt{a}$.
3. Decision Output: Print "YES" if no divisors are found (prime), otherwise "NO".

Complexity Analysis:
- Time: $\mathcal{O}(\sqrt{N})$ per test case - Trial division up to the square root of $n + 1$.
- Space: $\mathcal{O}(1)$ - Constant auxiliary space.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())

        a = n + 1
        possible = True

        # Primality test on n + 1
        if a < 2:
            possible = False
        else:
            i = 2
            while i * i <= a:
                if a % i == 0:
                    possible = False
                    break
                i += 1

        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()