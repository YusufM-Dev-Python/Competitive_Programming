import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: number of friends, h: height of the fence
    n, h = map(int, input().split())
    
    # List of heights of the friends
    s = list(map(int, input().split()))
    
    w = 0
    for i in range(n):
        # If friend is shorter or equal to fence, width is 1
        if s[i] <= h:
            w += 1
        # If friend is taller, they must bend, taking width 2
        else:
            w += 2
            
    print(w)

if __name__ == "__main__":
    solve()