"""
Day 135: Codeforces 1362B - Johnny and His Hobbies
Topic: Bit Manipulation / Brute Force
Logic:
1. Read the number of test cases `t`.
2. For each test case, read the size `n` and elements of the set `s`, storing them in a hash set for $O(1)$ lookups.
3. Iterate through all possible values of `k` from 1 up to 1024 (based on the problem constraints where elements are up to 1023, meaning XOR values stay within this range).
4. For each `k`, check if for every element `num` in the set, `num ^ k` also exists in the set.
5. The first `k` that satisfies this condition for all elements is the minimum valid value. If none found, print `-1`.

Complexity Analysis:
- Time: O(K * N) per test case, where K = 1024 and N is the size of the array. This easily runs well within the time limit.
- Space: O(N) - to store the set of elements.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))

        set_s = set(s)

        ans = -1
        for k in range(1, 1025):
            valid = True
            for num in s:
                if (num ^ k) not in set_s:
                    valid = False
                    break
            if valid:
                ans = k
                break
                
        print(ans)
        
if __name__ == '__main__':
    solve()