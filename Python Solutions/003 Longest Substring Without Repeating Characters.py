# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:53:01 2019

@author: Sue

003. Longest Substring Without Repeating Characters
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) <= 1):
            return len(s)
        
        res = 0
        #substring are [l..r)
        l = 0
        r = l + 1
        ls = list(s)

        while (l < len(s)) and (r <= len(s)) and (l <= len(s) - res):
            
            if (r == len(s)) or (ls[r] in ls[l:r]):
                #the substring from ls[l..r-1] is the longest
                res = max(res, r - l)
                l += 1
            else:
                r += 1
        return res
        
            