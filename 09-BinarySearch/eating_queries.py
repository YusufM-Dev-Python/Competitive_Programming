"""
Day 61 Starter: Eating Queries (Codeforces 1676E)
Logic:
1. Greedy: To minimize the number of candies, always eat the largest ones first.
2. Prefix Sums: Pre-calculate the cumulative sugar of the sorted candies.
3. Binary Search: For each query 'x', find the smallest index 'i' in the 
   prefix sum array such that prefix[i] >= x.

Complexity Analysis:
- Time: O((N + Q) * log N) - Sorting takes N log N, and Q queries take log N each.
- Space: O(N) - To store the prefix sum array.
"""

import sys

# Faster I/O for multiple queries
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Sort descending to eat the best candies first
        arr.sort(reverse=True)

        # Build Prefix Sum Array: prefix[i] is sum of first i candies
        prefix = [0] * (n + 1)  
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]

        for _ in range(q):
            query = int(input())

            # If the query is larger than the total sum, impossible
            if query > prefix[n]:
                print(-1)
                continue

            # Binary Search for the lower bound (smallest index >= query)
            l = 1
            r = n
            ans = -1

            while l <= r:
                mid = (l + r) // 2
                if prefix[mid] >= query:
                    ans = mid 
                    r = mid - 1 # Try to find an even smaller number of candies
                else:
                    l = mid + 1

            print(ans)

if __name__ == "__main__":
    solve()