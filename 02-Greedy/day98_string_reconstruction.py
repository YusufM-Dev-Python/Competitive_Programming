"""
Day 98: String Subsequence/Anagram Logic
Topic: Strings / Greedy
Logic:
1. Validate if 's' can be formed as a subset of characters from 't' using frequency maps.
2. If possible, partition the remaining characters of 't' into three groups:
   - 'small' (lexicographically smaller than s[0])
   - 'equal' (equal to s[0])
   - 'big' (lexicographically larger than s[0])
3. Greedily determine the optimal insertion point of 's' among the remaining characters 
   to achieve the lexicographically smallest result.

Complexity Analysis:
- Time: O(T * (|S| + |T| log |T|))
- Space: O(|T|)
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    T_input = input()
    if not T_input: return
    T = int(T_input)
    for _ in range(T):
        s = input()
        t = input()

        map_t = {}
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1
        
        possible = True
        for char in s:
            if map_t.get(char, 0) > 0:
                map_t[char] -= 1
            else:
                possible = False
                break

        if not possible:
            print("Impossible")
            continue

        # Sort remaining characters to bucket them
        left_t = sorted("".join(char * count for char, count in map_t.items()))
        small = "".join([c for c in left_t if c < s[0]])
        equal = "".join([c for c in left_t if c == s[0]])
        big = "".join([c for c in left_t if c > s[0]])
        
        # Decide placement
        printed = False
        for char in s:
            if s[0] < char:
                print(small + equal + s + big)
                printed = True
                break
            elif s[0] > char:
                print(small + s + equal + big)
                printed = True
                break
        
        if not printed:
            print(small + s + equal + big)

if __name__ == '__main__':
    solve()