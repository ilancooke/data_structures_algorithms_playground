'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dict
        # key=sorted version of the string
        # value = list of original strings that match sorted version
        # final answer is the dict's values
        results = defaultdict(list)
        for word in strs:
            word_list = sorted(word)
            sorted_word = ''.join(word_list)
            results[sorted_word].append(word)
        return list(results.values())