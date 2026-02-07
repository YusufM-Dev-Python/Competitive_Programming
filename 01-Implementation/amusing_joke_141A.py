import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Reading the guest name, residence host name, and the pile of letters
    s1 = input()
    s2 = input()
    s3 = input()
    
    # Logic: If the pile of letters contains exactly the same letters
    # as s1 and s2 combined, the sorted strings must be equal.
    if sorted(s1 + s2) == sorted(s3):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()