"""
Day 93: Spell Check (Codeforces 1722A)
Topic: Strings / Implementation / Sorting
Logic:
1. We need to check if a string of length 'n' is a valid anagram of the name "Timur".
2. The name "Timur" contains exactly 5 characters: 'T', 'i', 'm', 'u', 'r'.
3. Alphabetically sorting the string "Timur" yields "Imrtu" (uppercase 'T' comes 
   before lowercase letters in ASCII, but when sorted as a whole, 'I' comes first).
4. We verify if n == 5 and if the sorted input string exactly matches "Imrtu".

Complexity Analysis:
- Time: O(N log N) per test case - Sorting a string of length N. Since N is bounded by 5, this is O(1) in practice.
- Space: O(N) - To store the sorted string copy.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        
        # Alphabetically sorting "Timur" yields "Imrtu" due to ASCII values
        sorted_str = "".join(sorted(s))

        if n == 5 and sorted_str == "Imrtu":
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()