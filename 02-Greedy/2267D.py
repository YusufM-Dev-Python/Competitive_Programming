"""
Day 140: Codeforces 2267D - Greedy / Two Pointers / Parity Matching
Topic: Greedy / Sorting / Two Pointers
Logic:
1. Read the number of test cases `t`.
2. For each test case, read the size `n` and array `a`.
3. Pair each element with its 1-indexed parity (`(i + 1) % 2`) and sort the items by value.
4. Use two pointers (`lo` and `hi`) representing the available range of positions.
5. Greedily match each sorted element's parity with the available boundary parities, adjusting `lo` or `hi` accordingly. If a valid placement isn't possible, output "NO"; otherwise, print "YES".

Complexity Analysis:
- Time: O(N log N) per test case - due to sorting the items by value.
- Space: O(N) - to store the items list.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    items = []
    for i in range(n):
        val = a[i]
        parity = (i + 1) % 2 
        items.append((val, parity))

    items.sort(key=lambda x: x[0])
    
    lo = 1
    hi = n
    
    for val, p in items:
        lo_p = lo % 2
        hi_p = hi % 2
        
        if lo_p == hi_p:
            if p == lo_p:
                lo += 1
            else:
                print("NO")
                return
        else:
            if p == lo_p:
                lo += 1
            elif p == hi_p:
                hi -= 1
                
    print("YES")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()