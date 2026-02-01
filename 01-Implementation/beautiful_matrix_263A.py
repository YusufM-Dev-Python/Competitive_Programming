import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # The matrix is fixed at 5x5
    for i in range(5):
        # Read each row one by one
        line = list(map(int, input().split()))

        if 1 in line:
            # Found the '1', now find its column index
            c = line.index(1)
            r = i
            
            # Distance to center (2, 2) using Manhattan Distance formula:
            # |r1 - r2| + |c1 - c2|
            print(abs(r - 2) + abs(c - 2))
            # We can return early since there is only one '1'
            return

if __name__ == "__main__":
    solve()