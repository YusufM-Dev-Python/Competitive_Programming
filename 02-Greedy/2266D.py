"""
Day 139: Codeforces 2266D - Implementation / Sorting
Topic: Greedy / Sorting / Arrays
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array elements.
3. Compute the transformed values for each element based on its index: `arr[i] - (i + 1)`.
4. Remove duplicates and sort the unique transformed values.
5. Find the longest contiguous sequence where elements differ by 1, which represents the maximum valid steps or range, and print the maximum count.

Complexity Analysis:
- Time: O(N log N) per test case - due to sorting the unique transformed values.
- Space: O(N) - to store the array and the transformed set/list.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        ans = []
        steps = 0

        for i in range(n):
            ans.append(arr[i] - (i + 1))

        ans_n = sorted(list(set(ans)))
        
        max_steps = 1
        curr_steps = 1

        for i in range(1, len(ans_n)):
            if ans_n[i] == ans_n[i-1] + 1: 
                curr_steps += 1
            else:
                max_steps = max(max_steps, curr_steps)
                curr_steps = 1 

        print(max(max_steps, curr_steps))

if __name__ == '__main__':
    solve()