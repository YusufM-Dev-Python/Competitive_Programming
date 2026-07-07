"""
Day 95: Good Kid (Codeforces 1873B)
Topic: Greedy / Sorting
Logic:
1. To maximize the product of an array by adding 1 to exactly one element, 
   we should always target the smallest element.
2. Increasing the smallest value has the largest relative impact on the total product.
3. Your logic (prod * (arr[0] + 1)) correctly implements this.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Sort to easily access the minimum element at index 0
        arr.sort()
        
        # Increment the smallest element
        arr[0] += 1
        
        # Calculate the product of all elements
        prod = 1
        for x in arr:
            prod *= x
        print(prod)

if __name__ == "__main__":
    solve()