"""
Day 74 (Bonus): Fedor and New Game (Codeforces 467B)
Topic: Bit Manipulation
Logic:
1. Fedor's army is represented by the last integer in the input (arr[-1]).
2. To find the number of differing bits between Fedor and any other player, 
   we use the XOR (^) operator. 
   - XOR results in a '1' bit only where the bits of the two numbers differ.
3. We then count the number of set bits ('1's) in the result using bin().count('1').
4. If the count is <= k, the players can be friends.

Complexity Analysis:
- Time: O(M * log(max_N)) - We iterate through M players, and bit counting takes log(N) time.
- Space: O(M) - Storing the players' values in an array.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    # n: bits, m: players, k: max differing bits
    n, m, k = map(int, input().split())
    arr = []
    
    # Read m + 1 values (m players + Fedor)
    for _ in range(m + 1):
        x = int(input())
        arr.append(x)
    
    fedor = arr[-1]
    friends = 0
    
    # Compare each player with Fedor
    for i in range(m):
        # XOR shows the differences, count('1') counts them
        if bin(arr[i] ^ fedor).count('1') <= k:
            friends += 1
            
    print(friends)

if __name__ == "__main__":
    solve()