"""
Day 15: Odd Queries (Codeforces 1807D)
Problem Link: https://codeforces.com/contest/1807/problem/D

Logic:
We need to determine if the total sum of an array becomes odd after replacing 
a range [l, r] with a value 'k'.
1. Use Prefix Sums: Precalculate the cumulative sum of the array. This allows 
   us to find any range sum [l, r] in O(1) time.
2. Sum Replacement: The new total sum = (Original Total) - (Sum of Range [l, r]) 
   + (Length of Range * k).
3. Parity Check: If the new sum % 2 != 0, the answer is 'YES'.

Complexity Analysis:
- Time: O(N + Q) - O(N) to build prefix sums, O(Q) to answer queries.
- Space: O(N) - To store the prefix sum array.
"""

import sys

# Faster I/O is critical for problems with 2*10^5 queries
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))

        # Build Prefix Sum Array (1-based indexing for easier range queries)
        p = [0] * (n + 1)
        for i in range(n):
            p[i+1] = p[i] + a[i]

        total_sum = p[n]

        for _ in range(q):
            l, r, k = map(int, input().split())

            # Sum of the segment we are replacing
            old_range_sum = p[r] - p[l-1]
            
            # Count of elements in the range
            range_len = r - l + 1
            
            # Calculate the parity of the new total sum
            new_sum = total_sum - old_range_sum + (range_len * k)

            if new_sum % 2 != 0:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()