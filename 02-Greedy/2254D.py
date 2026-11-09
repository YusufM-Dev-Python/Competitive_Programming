"""
Day 170: Codeforces 2254D - Silhouette
Topic: Sorting / Grouping / Reconstruction / Greedy / Anti-hash

Question Extraction:
- Given a shadow array b of length n. b_i is the sum of all elements of the
  secret array a that are strictly smaller than a_i.
- Reconstruct the lexicographically smallest array a of strictly positive
  integers that produces b. If none exists, print -1.

Why we did this (Approach & Intuition):
- Equal a gives equal b (same set of smaller elements). A larger a gives a
  strictly larger b, because the smaller value is positive and adds to the
  sum. So each distinct b value corresponds to exactly one distinct value of a.
- Let the distinct values of a be x1 < x2 < ... < xk with counts c1 ... ck,
  and let B_j be the shadow of group j.
    B_1 = 0 (nothing is smaller than the minimum)
    B_{j+1} = B_j + c_j * x_j
  because "below the next group" = "below this group" + "this group itself".
- Rearranging: x_j = (B_{j+1} - B_j) / c_j. Every value except the last is
  forced by the shadows.
- The last group has no B_{k+1}, so it is the only free choice. For the
  lexicographically smallest array, take the smallest legal value:
  x_k = x_{k-1} + 1 (or 1 if there is only one group).
- Hashing: values go up to 2e14, and Codeforces has anti-hash tests, so every
  dict key is XORed with a random constant R. XOR is reversible, so
  (v ^ R) ^ R = v recovers the real value.

Logic:
1. Count each b value in dict m, using scrambled keys (v ^ R).
2. keys = sorted real values, recovered with k ^ R. Sort the REAL values, not
   the scrambled ones, since XOR destroys the order.
3. If keys[0] != 0, print -1.
4. For each group j except the last:
     diff = keys[j+1] - keys[j]    (total sum of group j)
     count = m[keys[j] ^ R]        (size of group j)
     -1 if diff % count != 0       (cannot split into equal integers)
     x = diff // count             (the VALUE of group j in a)
     -1 if x <= previous x         (values must strictly increase)
5. Append the last group's value, then map each original b[i] to its group's x
   via idx, so the output follows the input order.

Complexity:
- Time: O(n log n) per test (sorting), dict operations are expected O(1).
- Space: O(n).

Pitfalls hit while solving:
- Loop over distinct GROUPS, not over elements.
- Divide by the count of the CURRENT (lower) group, not the next one.
- After printing -1, use continue so the code does not fall through.
- set(b) hashes raw values and can be attacked, so recover keys from the
  scrambled dict (k ^ R) instead.
"""

import sys, random
input = lambda: sys.stdin.readline().rstrip()
R = random.getrandbits(48)

def solve():
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        m = {}
        for v in b:
            m[v ^ R] = m.get(v ^ R, 0) + 1

        keys = sorted(k ^ R for k in m)
        k = len(keys)
        if keys[0] != 0:
            out.append("-1")
            continue

        ans = []
        ok = True
        for j in range(k - 1):
            diff = keys[j + 1] - keys[j]
            count = m[keys[j] ^ R]
            if diff % count != 0:
                ok = False
                break
            x = diff // count
            if j > 0 and x <= ans[-1]:
                ok = False
                break
            ans.append(x)

        if not ok:
            out.append("-1")
            continue

        ans.append(ans[-1] + 1 if k > 1 else 1)
        idx = {keys[j] ^ R: j for j in range(k)}
        out.append(' '.join(str(ans[idx[v ^ R]]) for v in b))

    print('\n'.join(out))

if __name__ == "__main__":
    solve()