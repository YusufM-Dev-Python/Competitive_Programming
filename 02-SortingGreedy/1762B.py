"""
Day 73: Make Array Good (Codeforces 1762B)
Logic:
1. For any number a[i], we can find the smallest power of 2 (p) such that p >= a[i].
2. By adding (p - a[i]) to the element, we transform it into a power of 2.
3. Since any power of 2 divides a larger power of 2, this ensures the condition 
   a[i] | a[j] is easily met when elements are processed this way.
4. The problem allows up to n operations; this method uses at most n.

Complexity Analysis:
- Time: O(N log(max_A)) - Iterating through the array and finding the next power of 2.
- Space: O(N) - Storing the operations to be printed.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        ops = 0
        ans = []

        for i in range(n):
            p = 1
            while p < a[i]:
                p *= 2

            x = p - a[i]
            if x > 0:
                ans.append((i + 1, x))
                ops += 1
        
        print(ops)
        for i in range(ops):
            print(*ans[i])

if __name__ == "__main__":
    solve()