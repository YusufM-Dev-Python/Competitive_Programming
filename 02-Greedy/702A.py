"""
Day 75 (Bonus): Maximum Increase (Codeforces 702A)
Topic: Greedy / Implementation
Logic:
1. We maintain a 'curr_len' to track the length of the current strictly increasing subarray.
2. We iterate through the array starting from the second element.
3. If the current element is greater than the previous one (a[i] > a[i-1]), we increment 'curr_len'.
4. If not, the increasing sequence is broken, so we reset 'curr_len' to 1.
5. Throughout the process, 'max_len' stores the maximum value 'curr_len' has ever reached.

Complexity Analysis:
- Time: O(N) - A single linear scan through the array.
- Space: O(1) - Only a few variables used, excluding the input storage.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
        
    a = list(map(int,input().split()))
    curr_len = 1
    max_len = 1

    if n == 1:
        print(max_len)
    else:
        for i in range(1, n):
            if a[i] > a[i-1]:
                curr_len += 1
            else:
                curr_len = 1
            
            if curr_len > max_len:
                max_len = curr_len

        print(max_len)

if __name__ == "__main__":
    solve()