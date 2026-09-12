"""
Day 133: Codeforces 2263C1 - Range Filtering / Set Manipulation
Topic: Implementation / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array elements, and 1-index the array `a`.
3. Initialize a set `b_set` containing all numbers from `0` to `n - 1`.
4. For each index `k` from `1` to `n`, calculate the range `[start, end]` based on `k * ak`.
5. Remove any matching values within that range from `b_set`.
6. Print the count of remaining elements in `b_set` followed by the elements themselves.

Complexity Analysis:
- Time: O(N^2) worst-case depending on range sizes and set removals.
- Space: O(N) - to store the array and the set.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        a = [0] + arr
        b_set = set(range(n))
        
        for k in range(1, n + 1):
            ak = a[k]
            start = k * ak
            end = k * ak + k - 1
            
            for val in range(start, min(end + 1, n)):
                if val in b_set:
                    b_set.remove(val)
                    
        print(len(b_set))
        print(*(b_set))

if __name__ == "__main__":
    solve()