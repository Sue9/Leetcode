# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:39:02 2019

@author: Sue

17. Letter Combinations of a Phone Number
"""

class Solution(object):
        
    
    def formCombinations(self, digits, index, s, res):
        """
        :type digits: str
        :type index: int
        :type s: str, this contains one combination from digits[0..index-1]
        
        :rtype: void
        """
        
        if(index == len(digits)):
            res.append(s)
            return
        #print("digits[index] = ", digits[index])
        #print("self.letterMap[int(digits[index])])] = ", self.letterMap[ int(digits[index]) ])
        letterMap = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]    
        chars = letterMap[ int(digits[index]) ]
        for i in range(len(chars)):
            self.formCombinations(digits, index+1, s+chars[i], res)
        return
        
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(digits == ""):
            return []
        
        # digits is not empty
        res = []
        self.formCombinations(digits, 0, "", res)
        return res
        
        
        