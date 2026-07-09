"""
Day 96: Transfusion (Codeforces 2050B)
Topic: Implementation / Math
Logic:
1. The problem requires checking if the array can be leveled out or if specific 
   conditions regarding the averages of even and odd indexed elements hold true.
2. We iterate through the array once, keeping track of the running sum and 
   count for both even and odd indices.
3. Finally, we compare the integer averages (sum // count) and ensure there is 
   no remainder, effectively checking if the mean is an integer for both partitions.

Complexity Analysis:
- Time: O(N) - Single pass through the array.
- Space: O(1) - Using constant space for sums and counts.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        sum_even = 0
        sum_odd = 0
        count_even = 0
        count_odd = 0

        for j in range(n):
            if j % 2 == 0:
                sum_even += arr[j]
                count_even += 1
            else:
                sum_odd += arr[j]
                count_odd += 1
        
        # Verify if averages are equal and result in an integer
        if (sum_even / count_even) == (sum_odd / count_odd):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()