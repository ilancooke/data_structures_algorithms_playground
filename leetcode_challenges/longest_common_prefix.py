'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


'''
from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = max([len(word) for word in strs])
        current_longest_prefix = ''
        for i in range(max_length):
            # extract first n characters from all elements
            prefixes = [word[0:i+1] for word in strs]
            counts = Counter(prefixes)
            if counts.most_common(1)[0][1] == len(strs):
                # prefix is shared across all elements
                # make that prefix the new longest one
                current_longest_prefix = counts.most_common(1)[0][0]
            else:
                # prefix is not shared across all elements, so we can stop here
                break
        return current_longest_prefix