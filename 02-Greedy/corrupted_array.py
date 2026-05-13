"""
Day 65: Corrupted Array (Codeforces 1512D)
Logic:
1. We have an array of n+2 elements. One is the sum of n elements, one is "garbage" x.
2. Sort the array. The sum element is either arr[n+1] or arr[n].
3. Check Case 1: arr[n+1] is the sum. 
   Then Total_Sum(0 to n) must equal arr[n+1] if arr[n] was garbage, 
   OR (Total_Sum(0 to n+1) - some arr[i]) must equal arr[n+1].
4. Check Case 2: arr[n] is the sum.
   Then Total_Sum(0 to n-1) must equal arr[n].

Complexity Analysis:
- Time: O(N log N) for sorting.
- Space: O(N) to store the array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        # Array has n+2 elements
        arr = list(map(int, input().split()))
        arr.sort()

        # Total sum of the first n+1 elements
        sum_n_plus_1 = sum(arr[:n+1])

        # Case 1: The very last element arr[n+1] is the sum of n elements.
        # This means one element from arr[0...n] is garbage.
        found = False
        for i in range(n + 1):
            if sum_n_plus_1 - arr[i] == arr[n + 1]:
                # Found the garbage element at index i
                print(*(arr[:i] + arr[i+1:n+1]))
                found = True
                break
        
        if found:
            continue

        # Case 2: The second to last element arr[n] is the sum of n elements.
        # This implies arr[n+1] MUST be the garbage element.
        sum_n = sum(arr[:n])
        if sum_n == arr[n]:
            print(*(arr[:n]))
        else:
            print(-1)

if __name__ == "__main__":
    solve()