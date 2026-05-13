"""
Day 66: XXXXX (Codeforces 1364A)
Logic:
1. If the sum of the whole array isn't divisible by x, the answer is n.
2. If it is divisible, we need to remove a prefix or suffix to make the sum non-divisible.
3. The smallest prefix to remove is the one ending at the first element not divisible by x.
4. The smallest suffix to remove is the one starting at the last element not divisible by x.
5. If every single element is divisible by x, no subsegment will ever work (-1).

Complexity Analysis:
- Time: O(N) - Two linear scans (left to right and right to left).
- Space: O(N) - Storing the array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))

        total_sum = sum(arr)

        # Case 1: The whole array already works
        if total_sum % x != 0:
            print(n)
            continue
        
        # Case 2: Sum is divisible, find the first and last non-multiples
        l = -1
        r = -1

        # Find first index i where arr[i] % x != 0
        for i in range(n):
            if arr[i] % x != 0:
                l = i
                break
        
        # If no such element exists, any subarray sum will be divisible by x
        if l == -1:
            print(-1)
            continue

        # Find last index i where arr[i] % x != 0
        for i in range(n - 1, -1, -1):
            if arr[i] % x != 0:
                r = i
                break

        # Option 1: Remove prefix [0...l], remaining length = n - (l + 1)
        # Option 2: Remove suffix [r...n-1], remaining length = r
        print(max(n - l - 1, r))

if __name__ == "__main__":
    solve()