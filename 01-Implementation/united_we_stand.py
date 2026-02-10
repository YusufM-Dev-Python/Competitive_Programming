# Day 11: United We Stand (Codeforces 1859A)
# Folder: Implementation
# Logic: Smallest-Group Partition. By putting all occurrences of the 
# absolute minimum value into array 'b' and the rest into 'c', we 
# ensure no b[i] can divide any c[j] because c[j] > b[i].
# Time Complexity: O(n log n) - Due to sorting.
# Space Complexity: O(n) - Storing the two new arrays.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        l_a = int(input()) # Length of array a
        arr_a = list(map(int, input().split()))
        
        # Sort to isolate the smallest elements
        arr_a.sort()

        # If all elements are identical, we can't create two non-empty arrays
        if arr_a[0] == arr_a[-1]:
            print("-1")
            continue
        
        # Find the index where the value first jumps from the minimum
        idx = 0
        while idx < l_a and arr_a[idx] == arr_a[0]:
            idx += 1
            
        # b gets all the minimums, c gets everything larger
        b = arr_a[0:idx] 
        c = arr_a[idx:]

        # Output the lengths and the elements
        print(len(b), len(c))
        print(*b)
        print(*c)

if __name__ == "__main__":
    solve()