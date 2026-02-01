import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Convert entire string to lower case immediately
    n = str(input()).lower()
    
    # "Y" is considered a vowel in this problem
    vowels = "aeiouy"
    
    for char in n:
        if char in vowels:
            # Delete (skip) vowels
            continue
        else:
            # For consonants: print a dot followed by the character
            # end="" keeps everything on the same line
            print(f".{char}", end="")
    
    # Optional: print a newline at the end for clean output
    print()

if __name__ == "__main__":
    solve()