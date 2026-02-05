import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: number of magnets
    n = int(input())

    # We read the first magnet to set the initial state
    prev = str(input())
    groups = 1

    # We iterate through the remaining n-1 magnets
    for _ in range(n - 1):
        curr = str(input())

        # If the current magnet is different from the previous one,
        # it means they don't "fit" into the same group.
        if curr != prev:
            groups += 1
        
        # Update the 'prev' state for the next comparison
        prev = curr
        
    print(groups)

if __name__ == "__main__":
    solve()