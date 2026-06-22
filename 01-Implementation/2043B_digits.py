"""
Day 84: Factorial Digit Divisibility
Topic: Math / Number Theory
Logic:
1. 1 always divides any number, so it is appended unconditionally.
2. For 3: A number is divisible by 3 if the sum of its digits is a multiple of 3. 
   The sum of digits here depends on n! * d. If n >= 3, n! contains 3 as a factor, 
   making the total sum divisible by 3 regardless of d. Otherwise, d must be divisible by 3.
3. For 5: The number ends with digit d, so it is divisible by 5 if and only if d == 5.
4. For 7: A repeating digit number is divisible by 7 if the count of repeating blocks 
   is a multiple of 6. Since n! contains a factor of 6 for any n >= 3, it works. 
   Alternatively, if d == 7, it always works.
5. For 9: Similar to 3, but requires the sum of digits to have two factors of 3.

Complexity Analysis:
- Time: O(1) per test case - Uses simple conditional statements.
- Space: O(1) - Constant memory allocated for storing at most 5 elements.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        ans = []

        ans.append(1)

        if n >= 3 or d % 3 == 0:
            ans.append(3)
        
        if d == 5:
            ans.append(5)
        
        if n >= 3 or d == 7:
            ans.append(7)

        if n >= 6 or (n >= 3 and d % 3 == 0) or d == 9:
            ans.append(9)

        print(*ans)

if __name__ == "__main__":
    solve()