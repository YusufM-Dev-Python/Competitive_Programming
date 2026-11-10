"""
Day 171: Codeforces 2280B - Interactive Binary String (find a "01")
Topic: Interactive / Observation / Binary String / Counting

Question Extraction:
- There is a hidden binary string s of length n.
- Decide whether there exists an index i (1 <= i < n) with s_i = 0 and
  s_{i+1} = 1, i.e. whether "01" appears as a substring.
- Allowed query: "? l r" returns the number of 1s in s[l..r].
- At most 5 queries per test case. Answer with "! YES" or "! NO".

Why we did this (Approach & Intuition):
- Flip the question: when does the string NOT contain "01"?
  If no 0 is ever directly followed by a 1, then once a 0 appears, every
  character after it must also be 0. So the string must look like
      1...1 0...0   (some 1s, then some 0s)
  and any other string contains "01".
- Let c = total number of 1s in s. Query (1, n) gives c.
  If s has the form 1^c 0^(n-c), then the first c characters are all 1s.
  If s is not of that form, some 1 sits beyond position c, so a 0 must
  appear within the first c positions and the string has a "01".
- So one extra query on the prefix [1, c] settles it:
    count of 1s in s[1..c] == c  ->  prefix is all 1s  ->  form 1^c 0^(n-c)  ->  NO
    count of 1s in s[1..c] <  c  ->  a 0 hides inside the prefix and
                                     some 1 comes after it     ->  YES
- Edge case c = 0: all zeros, no 1 exists, so no "01" -> NO. This avoids
  querying (1, 0), which would be invalid.

Logic:
1. c = ask(1, n).
2. If c == 0: answer NO.
3. Else if ask(1, c) == c: the string is 1^c 0^(n-c), answer NO.
4. Otherwise answer YES.

Complexity:
- Queries: at most 2 per test case (limit is 5).
- Time: O(1) per test case besides interaction. Space: O(1).

Pitfalls hit while solving:
- Flush after every print (flush=True), otherwise Idleness limit exceeded.
- If the judge returns -1, exit immediately so the code does not read from
  a closed stream.
- Never call ask(1, 0). The c == 0 check must come first.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def ask(l, r):
    print(f"? {l} {r}", flush=True)
    res = int(input())
    if res == -1:
        sys.exit()
    return res

def ans(yes):
    print("! YES" if yes else "! NO", flush=True)

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        c = ask(1, n)
        if c == 0:
            ans(False)
        elif ask(1, c) == c:
            ans(False)
        else:
            ans(True)

if __name__ == "__main__":
    solve()