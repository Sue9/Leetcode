# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:44:56 2018

@author: zhaoxu

022 Generate Parentheses

point is, 'valid': the number of left parentheses >= the number of right parentheses
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n == 0:
            return [""]
        
        res = []
        self.dfs(n, n, '', res)
        return res
        
        
    
    def dfs(self, l, r, item, res):
        """
        @param l: left num that have not been used
        @param r: right num that have not been used
        @param item: the string we have so far
        @param res: result, List[str]
        """
        if l > r:
            return
        
        if (l == 0) and (r == 0):
            res.append(item)
            
        if l > 0:
            self.dfs(l - 1, r, item+'(', res)
        
        if r > 0:
            self.dfs(l, r - 1, item+')', res)
        

