"""
Day 97: 2067B - Two Large Bags
Topic: Greedy / Frequency Array
Logic:
1. Count the occurrences of each number.
2. If any count is 1, it's impossible to form a pair, so output "No".
3. If a count is > 2, carry the excess (count - 2) over to the next number (i + 1),
   as we can always convert two numbers of value 'i' into two numbers of value 'i+1'.
4. If we process all values without hitting a count of 1, output "Yes".
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Use fast I/O
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Frequencies up to n+1 to handle the carry-over
        freq = [0] * (n + 2)
        for x in arr:
            freq[x] += 1
            
        possible = True
        for i in range(1, n + 1):
            if freq[i] == 1:
                possible = False
                break
            elif freq[i] > 2:
                # Carry excess to the next number
                freq[i + 1] += freq[i] - 2
        
        print("Yes" if possible else "No")

if __name__ == '__main__':
    solve()