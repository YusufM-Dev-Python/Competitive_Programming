import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # k, l, m, n: damage intervals
    # d: total number of dragons
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())

    hitted = 0
    # Iterate through every dragon from 1 to d
    for i in range(1, d + 1):
        # If the dragon index is a multiple of any of the damage values
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            hitted += 1
        
    print(hitted) 

if __name__ == "__main__":
    solve()