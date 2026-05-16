'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

    1 <= s1.length, s2.length <= 10^4
    s1 and s2 consist of lowercase English letters.

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Store character counts for the current sliding window.
        count = {}
        # Left boundary of the sliding window.
        left = 0
        # Move the right boundary across the string one character at a time.
        for right in range(len(s2)):
            # Add the right character to the current window count.
            count[s2[right]] = 1 + count.get(s2[right], 0)

            # If the window size exceeds s1's length, shrink it from the left.
            if right - left + 1 > len(s1):
                count[s2[left]] -= 1
                left += 1

            # Check if the current window's character counts match s1's counts.
            if count == {c: s1.count(c) for c in set(s1)}:
                return True

        # If we finish checking all windows without finding a match, return False.
        return False