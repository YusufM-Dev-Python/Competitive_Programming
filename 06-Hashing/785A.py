"""
Day 85: Anton and Polyhedrons (Codeforces 785A)
Topic: Implementation / Hash Maps
Logic:
1. We predefine a dictionary mapping each type of polyhedron to its respective number of faces.
2. We loop 'n' times to read each polyhedron Anton has collection.
3. For each shape, we look up its value in our dictionary in O(1) time and accumulate it into 'total'.

Complexity Analysis:
- Time: O(N) - Single loop iterating through N inputs.
- Space: O(1) - The space used by the dictionary is fixed (only 5 static key-value pairs).
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    # Mapping polyhedron names to their face counts
    faces = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20
    }

    total = 0
    n = int(input())
    for _ in range(n):
        shape = input()
        total += faces[shape]

    print(total)

if __name__ == "__main__":
    solve()