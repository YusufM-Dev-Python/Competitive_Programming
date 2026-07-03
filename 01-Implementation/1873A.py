"""
Day 90: Short Sort (Codeforces 1873A)
Topic: Strings / Implementation / Brute Force
Logic:
1. The target string is "abc". We can perform at most one swap of two letters.
2. If a string can become "abc" in 0 or 1 swaps, at least one of its characters 
   must already be sitting in its final correct index position.
3. We check if the first character is 'a', the second is 'b', or the third is 'c'.
4. If at least one condition holds true, we print "YES". Otherwise, we print "NO".

Complexity Analysis:
- Time: O(1) per test case - Fixed string length of 3 eliminates any loop scaling.
- Space: O(1) - Constant workspace memory allocation.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        
        # If any character matches its position in "abc", it takes <= 1 swap
        if s[0] == 'a' or s[1] == 'b' or s[2] == 'c':
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()