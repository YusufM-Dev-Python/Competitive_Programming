"""
Day 92: Vanya and Cubes (Codeforces 492A)
Topic: Implementation / Simulation / Math
Logic:
1. We want to construct a pyramid of maximum height using at most 'n' cubes.
2. The i-th level requires (i * (i + 1)) // 2 cubes (the i-th triangular number).
3. We iteratively calculate the cubes needed for the next layer (next_height).
4. If our remaining pool of cubes allows it, we add these to cubes_used and increment our height.
5. The loop terminates when building the next layer would exceed 'n' total cubes.

Complexity Analysis:
- Time: O(H) where H is the maximum height of the pyramid. Since the sum scales cubically 
        as O(H^3), for n <= 10,000, H will be at most ~40, making this O(1) in practice.
- Space: O(1) - Constant memory overhead used for basic scalar tracking.
"""

import sys

def main():
    # Read the number of available cubes
    n = int(sys.stdin.read().strip())
    
    current_height = 0
    cubes_used = 0
    
    while True:
        next_height = current_height + 1
        # Cubes needed for the next level: 1 + 2 + ... + next_height
        cubes_needed_for_level = (next_height * (next_height + 1)) // 2
        
        if cubes_used + cubes_needed_for_level <= n:
            cubes_used += cubes_needed_for_level
            current_height = next_height
        else:
            break
            
    print(current_height)

if __name__ == '__main__':
    main()