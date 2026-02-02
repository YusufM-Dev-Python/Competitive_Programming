import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    # line[i] represents who child (i+1) gave a gift to.
    line = list(map(int, input().split()))
    result = [0] * n

    for i in range(n):
        giver = i + 1      # The person currently being looked at
        taker = line[i] - 1 # The index of the person who received the gift

        # The result array needs to store who GAVE a gift to person 'taker'
        result[taker] = giver 
        
    # Pythonic way to print list elements separated by spaces
    print(*result)

if __name__ == "__main__":
    solve()