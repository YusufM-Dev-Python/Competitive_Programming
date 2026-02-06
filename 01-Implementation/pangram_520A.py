import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    
    # Case insensitivity is key: .lower() handles "A" vs "a"
    s = input().lower()
    
    # A set only stores unique elements
    new_set = set(s)
    
    # If the number of unique characters is 26, it's a pangram
    if len(new_set) == 26:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()