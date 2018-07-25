# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:15:27 2018

@author: zhaoxu

Leetcode 344. Reverse String

Q: what's the difference between range and xrange?
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

"""
Solution 3: recursive way. Runtime: 112ms
"""
        
        if(len(s) == 1)or(len(s) == 0):
            return s
        
        left = self.reverseString(s[:int(len(s)/2)])
        right = self.reverseString(s[int(len(s)/2):])
        
        return right+left
        
    
"""
Solution 1: This is the quickest. Runtime: 24ms

        return s[::-1]



Solution 2: Two pointers. Runtime = 40ms
    
        s = list( s )

        for i in range(int(len(s) / 2)):
            left = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = left
        return ''.join(s)
"""    