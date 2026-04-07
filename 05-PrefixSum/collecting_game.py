"""
Day 50 Milestone: Collecting Game (CF 1904B)
Logic:
- Sorting + Prefix Sums to determine total power at any index.
- Suffix propagation (Reach array) to see how far the "chain reaction" goes.
- O(N log N) total time.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    for _ in range(int(t_str)):
        n = int(input())
        # Pairing values with original indices is crucial for Problem B/C tasks
        arr = sorted([[v, i] for i, v in enumerate(map(int, input().split()))])

        prefix = [0] * n
        prefix[0] = arr[0][0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i][0]
        
        reach = [0] * n
        reach[n-1] = n - 1
        # Suffix propagation: The "Magic" of the solution
        for i in range(n-2, -1, -1):
            if prefix[i] >= arr[i+1][0]:
                reach[i] = reach[i+1]
            else:
                reach[i] = i
        
        # Placing the results back into a result array based on original index
        ans = [0] * n
        for i in range(n):
            ans[arr[i][1]] = reach[i]
        print(*ans)

if __name__ == "__main__":
    solve()