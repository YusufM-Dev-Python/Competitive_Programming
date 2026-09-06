"""
Day 132: 581A - Vasya the Hipster
Topic: Math / Implementation
Goal: Calculate the maximum days Vasya can wear different-colored socks 
      and the subsequent days he can wear same-colored socks.

Logic:
1. Different-Colored Days: Vasya pairs one red and one blue sock each day, 
   so the maximum count is limited by the smaller sock count: `min(a, b)`.
2. Same-Colored Days: Take the absolute difference between `a` and `b`, 
   divide by 2 (`// 2`), since each pair of same-colored socks requires 2 socks.
3. Output: Print both values separated by a space.

Complexity Analysis:
- Time: $\mathcal{O}(1)$ - Constant time arithmetic operations.
- Space: $\mathcal{O}(1)$ - Constant memory space.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    a, b = map(int, input().split())

    # min(a, b) gives different colored days; remainder // 2 gives same colored days
    print(min(a, b), abs(a - b) // 2)
    
if __name__ == "__main__":
    solve()