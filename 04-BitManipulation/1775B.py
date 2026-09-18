"""
Day 137: Codeforces 1775B - Gardener and the Array
Topic: Hash Maps / Implementation / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` sequences, storing each sequence's elements and counting the global frequency of every element across all sequences using a hash map (`freq`).
3. Iterate through each sequence to check if there exists at least one sequence where every element has a frequency strictly greater than 1 (`freq[pos] > 1`). 
4. If such a sequence is found, it means every element it contains is covered by at least one other sequence, so we can remove it, making the answer "YES". Otherwise, print "NO".

Complexity Analysis:
- Time: O(sum of k) per test case - where k is the size of each sequence, iterating through all elements to build frequencies and check them.
- Space: O(total elements across all sequences) - to store the sequences and the frequency map.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        freq = {}
        
        for _ in range(n):
            line = list(map(int, input().split()))
            k = line[0]
            positions = line[1:]
            arr.append(positions)

            for pos in positions:
                freq[pos] = freq.get(pos, 0) + 1
            
        ans = "NO"
        for positions in arr:
            is_there = True
            for pos in positions:
                if freq[pos] == 1:
                    is_there = False
                    break

            if is_there:
                ans = "YES"
                break
        
        print(ans)
        
if __name__ == "__main__":
    solve()