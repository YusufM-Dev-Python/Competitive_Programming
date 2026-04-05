"""
Day 48: Raspberries (Codeforces 1883C)
Problem Link: https://codeforces.com/contest/1883/problem/C

Logic:
1. We want the product of elements to be divisible by k.
2. For prime k (2, 3, 5), we find the min operations to make 
   at least one element divisible by k.
3. For composite k = 4, there are two ways:
   a) Make one element a multiple of 4.
   b) Make at least two elements multiples of 2 (since 2*2=4).
4. Track the number of even elements to handle the k=4 special case.

Complexity Analysis:
- Time: O(N) per test case.
- Space: O(N) to store the array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        min_step = k  # Max possible steps needed is k
        evens = 0
        already_divisible = False

        for x in arr:
            if x % k == 0:
                already_divisible = True
            
            # Distance to the next multiple of k
            rem = x % k
            min_step = min(min_step, (k - rem) % k)
            
            # Count evens for the k=4 case
            if x % 2 == 0:
                evens += 1

        if already_divisible:
            print(0)
            continue

        if k != 4:
            print(min_step)
        else:
            # Special case k=4: either make one element a multiple of 4
            # OR make two elements multiples of 2.
            # Steps to get two evens:
            if evens >= 2:
                two_even_steps = 0
            elif evens == 1:
                two_even_steps = 1
            else:
                two_even_steps = 2
            
            print(min(min_step, two_even_steps))

if __name__ == '__main__':
    solve()