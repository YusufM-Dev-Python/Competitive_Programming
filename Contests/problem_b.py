"""
Day 47: Codeforces Round 1090 (Div. 4) - Problem B
Problem Link: (Pending Official Name/Link)

Logic:
1. For each test case, we receive an array of 7 integers.
2. Sorting the array allows us to easily access the smallest 
   and largest values.
3. The logic involves negating the 6 smallest values and 
   adding them to the largest value to find the final answer.
4. This effectively calculates: Largest - (Sum of others).

Complexity Analysis:
- Time: O(T) - Sorting 7 elements is constant time.
- Space: O(1) - Fixed size array storage.
"""

import sys

# Faster I/O for contest environments
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        # Read the 7 integers provided in the problem
        arr = list(map(int, input().split()))
        sorted_arr = sorted(arr)
        
        # ans_arr will store the negated versions of the first 6 elements
        ans_arr = [0] * 6

        for i in range(6):
            ans_arr[i] = sorted_arr[i] * (-1)
        
        # Final result: Sum of negated smalls + the largest element
        # Mathematically equivalent to: sorted_arr[6] - sum(sorted_arr[0:6])
        print(sum(ans_arr) + sorted_arr[6])

if __name__ == "__main__":
    solve()