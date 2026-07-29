"""
Day 114 (Part 2): 1519C - Berland Regional (Sorting & Prefix Sums)
Topic: Sorting / Prefix Sums / Harmonic Series Optimization
Goal: Find the maximum total skill sum for each team size k (from 1 to n) 
      when grouping students by university and discarding extras that don't fit the size constraint.

Logic:
1. Grouping: Use a defaultdict to group students' skills by their respective university.
2. Sorting & Prefix Sums: For each university, sort the skills in descending order and 
   compute a prefix sum array to allow $\mathcal{O}(1)$ range sum queries.
3. Harmonic Series Optimization: For team size `k`, the number of students we can use from a university 
   of size `m` is `valid_count = m - (m % k)`. Summing this over all team sizes takes $\mathcal{O}(N \log N)$ 
   time because $\sum \frac{N}{k} \approx N \log N$.
4. Aggregate totals into an answer array and print results from size 1 to n.

Complexity Analysis:
- Time: $\mathcal{O}(N \log N)$ overall due to sorting each university's list and the harmonic series traversal.
- Space: $\mathcal{O}(N)$ to store student groups, prefix sums, and answer arrays.
"""

from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        u = list(map(int, input().split()))
        s = list(map(int, input().split())) 

        uni_groups = defaultdict(list)
    
        # Step 1: Group students' skills by their university
        for i in range(n):
            uni_groups[u[i]].append(s[i])
        
        ans = [0] * (n + 1) 

        # Step 2: Process each university group
        for skills in uni_groups.values():
            skills.sort(reverse=True) # Sort skills descending to pick the best first
            m = len(skills)
        
            # Build prefix sums for fast range sum retrieval
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = pref[i] + skills[i]

            # Step 3: Evaluate for each team size k using harmonic series optimization
            for k in range(1, m + 1):
                valid_count = m - (m % k)  # Drop students who cannot fit into a full team of size k
                ans[k] += pref[valid_count]
            
        # Print results for team sizes 1 through n
        print(*(ans[1:]))

if __name__ == "__main__":
    solve()