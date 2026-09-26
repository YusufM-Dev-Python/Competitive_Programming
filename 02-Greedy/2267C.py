"""
Day 141: Codeforces 2267C - Number Theory / Divisors
Topic: Number Theory / Hash Map / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `x`, along with the array elements `arr`.
3. Find all divisors of `x` (excluding 1) using trial division up to $\sqrt{x}$.
4. Use a hash map (`mpp`) to accumulate the sum of array elements that are multiples of each divisor.
5. Find the maximum sum among all valid divisors and print it (`max(mpp.values())` if map is non-empty, otherwise 0).

Complexity Analysis:
- Time: O(N * num_divisors(X) + \sqrt{X}) per test case - finding divisors of X and iterating through the array to check divisibility.
- Space: O(num_divisors(X)) - to store the divisors list and the frequency/sum map.
"""

from collections import defaultdict
import math
import sys

input = lambda: sys.stdin.readline().strip()

def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))

        divisor = []
        limit = int(math.isqrt(x))

        for i in range(2, limit + 1):
            if x % i == 0:
                divisor.append(i)
                if i != x // i:
                    divisor.append(x // i)
                    
        if x != 1:
            divisor.append(x)
            
        mpp = defaultdict(int)

        for num in arr:
            for d in divisor:
                if d == 1:
                    continue
                if num % d == 0:
                    mpp[d] += num

        ans = 0
        if mpp:
            ans = max(mpp.values())
        print(ans)

if __name__ == "__main__":
    solve()