'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointer solution
        left = 0
        seen = set()
        max_length = 0
        for right in range(len(s)):
            current_char = s[right]
            while current_char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(current_char)
            current_window_length = right - left + 1
            max_length = max(max_length, current_window_length)
        return max_length