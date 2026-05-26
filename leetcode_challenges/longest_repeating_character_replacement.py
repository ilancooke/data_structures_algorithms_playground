'''
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

 

Constraints:

    1 <= s.length <= 10^5
    s consists of only uppercase English letters.
    0 <= k <= s.length

'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Store character counts for the current sliding window.
        count = {}
        # Track the longest valid window length seen so far.
        res = 0
        # Left boundary of the sliding window.
        left = 0
        # Move the right boundary across the string one character at a time.
        for right in range(len(s)):
            # Add the right character to the current window count.
            count[s[right]] = 1 + count.get(s[right], 0)

            # If replacements needed exceeds k, shrink the window from the left.
            while (right-left+1) - max(count.values()) > k:
                # Remove the left character from the current window count.
                count[s[left]] -= 1
                # Move the left boundary rightward to shrink the window.
                left += 1

            # Update the best answer with the current valid window length.
            res = max(res, right-left+1)
        # Return the length of the longest valid window.
        return res
