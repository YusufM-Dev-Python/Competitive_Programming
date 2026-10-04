"""
Day 149: Codeforces 1372B - Omkar and Last Class of Math
Topic: Number Theory / Math
Logic:
1. Read the number of test cases `t`.
2. For each test case, read integer `n`.
3. If `n` is even, the optimal split is simply `n // 2` and `n // 2` (since their LCM is minimized at `n // 2`).
4. If `n` is odd, find all divisors up to $\sqrt{n}$. To minimize the LCM of `a` and `b` where `a + b = n`, we want to maximize the largest proper divisor of `n` (which is equivalent to finding the smallest prime factor).
5. If no proper divisors exist (meaning `n` is prime), the split is `1` and `n - 1`. Otherwise, the split is `max_ans` and `n - max_ans`.

Complexity Analysis:
- Time: O(\sqrt{N}) per test case - trial division up to the square root of `n`.
- Space: O(num_divisors(N)) - to store the divisors list.
"""

import sys
import math

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        divisors = []

        for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)

        max_ans = float('-inf')

        if n % 2 == 0:
          print(f"{n//2} {n//2}")
        else:
          for i in divisors:
            curr_ans = n // i
            max_ans = max(max_ans, curr_ans)
            
          if max_ans == float("-inf"):
            print(f"1 {n - 1}")
          else:
            print(f"{max_ans} {n - max_ans}")          

if __name__ == "__main__":
    solve()