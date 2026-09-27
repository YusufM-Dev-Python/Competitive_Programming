"""
Day 142: Mock ICPC - Taha Bhai and the Angel Shots
Topic: Binary Search on Answer / Greedy
Logic:
1. Read the number of bartenders `n` and target angel shots `s`, along with prepare times `a` and rest times `b`.
2. Use binary search on the possible total time `T` (ranging from `0` to `2 * 10^18`).
3. In the helper function `can_make(T)`, calculate how many shots each bartender can produce in time `T`. Since a bartender doesn't need to rest after their final shot, the number of shots is given by `(T + b) // (a + b)`.
4. Sum the shots across all bartenders. If the total is at least `s`, return True.
5. Narrow down the search range to find the minimum possible time `ans`.

Complexity Analysis:
- Time: O(N log(HIGH)) per test case - where HIGH is $2 \times 10^{18}$, and checking takes O(N).
- Space: O(N) - to store the prepare and rest time arrays.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    def can_make(T):
        total_shots = 0
        for i in range(n):
            shots = (T + b[i]) // (a[i] + b[i])
            total_shots += shots
            if total_shots >= s:
                return True
        return total_shots >= s

    low = 0
    high = 2 * 10**18 
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_make(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)

if __name__ == "__main__":
    solve()