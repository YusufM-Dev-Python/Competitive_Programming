import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n can be up to 10^15, so O(1) is mandatory
    n = int(input())
    
    # Pattern:
    # f(1) = -1
    # f(2) = -1 + 2 = 1
    # f(3) = -1 + 2 - 3 = -2
    # f(4) = -1 + 2 - 3 + 4 = 2
    # Even n: n/2
    # Odd n: -(n+1)/2
    
    if n % 2 == 0:
        print(n // 2)
    else:
        print(-(n + 1) // 2)

if __name__ == "__main__":
    solve()