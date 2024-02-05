'''
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = {}

        for ch in s:
            cache[ch] = cache.get(ch, 0) + 1
            
        for index in range(len(s)):
            if cache[s[index]] == 1:
                return index
        return -1