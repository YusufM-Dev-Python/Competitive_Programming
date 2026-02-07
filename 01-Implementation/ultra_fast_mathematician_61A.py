import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Reading two strings of 0s and 1s
    s1 = input()
    s2 = input()

    # The Python Magic:
    # 1. zip(s1, s2) pairs up the bits: (s1[0], s2[0]), (s1[1], s2[1])...
    # 2. "1" if a != b else "0" performs the XOR logic.
    # 3. "".join(...) collects the generator results into a single string efficiently.
    result = "".join("1" if a != b else "0" for a, b in zip(s1, s2))
    
    print(result)

if __name__ == "__main__":
    solve()