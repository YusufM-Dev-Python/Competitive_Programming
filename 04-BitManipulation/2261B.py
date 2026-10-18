"""
Day 159: Codeforces 2261B - Bitwise Greedy Span Optimization
Topic: Bit Manipulation / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array `a`.
3. Iterate from bit position `30` down to `0` using a greedy bitwise approach:
   - If *all* elements in `a` have the current bit set (`all(x & bit for x in a)`), set that bit in our answer (`ans |= bit`).
   - If *any* (but not all) elements have the bit set (`any(x & bit for x in a)`), we can fill all lower bits up to the maximum possible range using `(bit << 1) - 1`, and break out of the loop.
4. Print the final computed value `ans`.

Complexity Analysis:
- Time: O(31 \times N) per test case - constant 31 bit iterations checking elements linearly.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = 0
        for b in range(30, -1, -1):
            bit = 1 << b
            if all(x & bit for x in a):  
                ans |= bit
            elif any(x & bit for x in a):  
                ans |= (bit << 1) - 1        
                break
        print(ans)

if __name__ == "__main__":
    solve()