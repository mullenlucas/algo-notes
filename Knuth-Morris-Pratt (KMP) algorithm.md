28. ## Find the Index of the First Occurrence in a String



Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**

**Input:** haystack = "sadbutsad", needle = "sad"
**Output:** 0
**Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

**Example 2:**

**Input:** haystack = "leetcode", needle = "leeto"
**Output:** -1
**Explanation:** "leeto" did not occur in "leetcode", so we return -1.



#### Straightforward solution

1. Check if the `needle` string is `in` the `haystack` string

2. If so, check for the first index of appearence.

3. Otherwise, return -1



```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
```



## Knuth-Morris-Pratt (KMP) algorithm

which can be more optimal for large strings or cases where the `needle` is long.

The KMP algorithm is based on pattern matching and utilizes a prefix table (also known as the "failure function") to avoid unnecessary backtracking when searching for the pattern. This makes it more efficient than the `in` operator followed by `index()` for certain cases.

The Knuth-Morris-Pratt (KMP) algorithm is a pattern matching algorithm that efficiently finds occurrences of a pattern (needle) within a larger text (haystack). It avoids unnecessary backtracking during the search, making it more efficient than naive pattern matching methods.

Let's walk through the steps of the KMP algorithm:

#### Step 1: Build the Prefix Table

The key idea behind the KMP algorithm is to build a prefix table (also known as the "failure function" or "partial match table") from the pattern (needle). The prefix table stores information about the longest proper prefix (excluding the whole string) that is also a suffix of the pattern.

For example, consider the pattern "ABABCAB". The prefix table for this pattern is [0, 0, 1, 2, 0, 1, 2]. Each value in the prefix table represents the length of the longest proper prefix that is also a suffix for the substring ending at that position.

To build the prefix table, you can use the following algorithm:

```python
def build_prefix_table(pattern):
    prefix_table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            prefix_table[i] = j
        else:
            if j > 0:
                j = prefix_table[j - 1]
                i -= 1
            else:
                prefix_table[i] = 0

    return prefix_table

```



#### Step 2: Search the Pattern in the Text

Once you have built the prefix table, you can use it to efficiently search for the pattern (needle) in the text (haystack) without unnecessary backtracking.

The search process uses two pointers, `i` for the text and `j` for the pattern. You start with both pointers at the beginning of their respective strings. Then, you iteratively compare characters of the text and the pattern:

```python
def strStr(haystack, needle):
    if not needle:
        return 0

    prefix_table = build_prefix_table(needle)
    i = j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j
        else:
            if j > 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return -1

```



The search process works as follows:

- If the characters at positions `i` and `j` match, move both pointers `i` and `j` one step forward.
- If `j` reaches the end of the pattern, it means we found a match, and we return the starting index of the match (i - j).
- If the characters at positions `i` and `j` do not match:
  - If `j > 0`, update `j` using the prefix table to avoid unnecessary comparisons. It means we shift the pattern to the right by an amount `j - prefix_table[j-1]` (the amount of characters already matched).
  - If `j` is already at the beginning of the pattern, move the `i` pointer one step forward.

By using the prefix table, the KMP algorithm avoids rechecking characters that are already known to match, which significantly improves the efficiency of the pattern search.

The KMP algorithm runs in O(n + m) time complexity, where n is the length of the text (haystack) and m is the length of the pattern (needle). This makes it more efficient than the naive approach that would take O(n * m) time complexity in the worst case.
