import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read the word
    w = str(input()).strip()

    # Abbreviation logic: only for words strictly longer than 10 characters
    if len(w) > 10:
        f = w[0]           # First character
        m = len(w) - 2     # Count of characters in between
        l = w[-1]          # Last character (shorthand for w[len(w)-1])
        print(f"{f}{m}{l}")
    else:
        print(w)

if __name__ == "__main__":
    try:
        line = input()
        if line:
            # First line is the number of test cases
            t = int(line)
            for _ in range(t):
                solve()
    except ValueError:
        pass