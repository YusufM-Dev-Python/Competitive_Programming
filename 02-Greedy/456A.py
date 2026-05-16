"""
Day 78: Laptops (Codeforces 456A)
Topic: Sorting / Greedy
Logic:
1. Alex claims there is a laptop that is cheaper but has higher quality than another laptop.
2. We store the laptops as tuples of (price, quality) and sort them by price.
3. Once sorted by price, we check if any laptop has a lower quality than the laptop right before it.
4. Since price[i-1][0] <= price[i][0], if price[i-1][1] > price[i][1], then laptop i-1 is cheaper 
   but has a strictly higher quality than laptop i. This satisfies Alex's condition.

Complexity Analysis:
- Time: O(N log N) - Due to sorting the laptops array.
- Space: O(N) - Storing the laptop pairs.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    price = []
    for _ in range(n):
        a, b = map(int, input().split())
        price.append((a, b))
    
    # Sort primarily by price
    price.sort(key=lambda p: p[0])
    
    flag = False
    for i in range(1, n):
        # If a cheaper laptop has a higher quality than a more expensive one
        if price[i-1][1] > price[i][1]:
            flag = True
            break
    
    if flag:
        print("Happy Alex")
    else:
        print("Poor Alex")

if __name__ == "__main__":
    solve()