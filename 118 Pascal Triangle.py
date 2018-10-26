# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:20:42 2018

@author: zhaoxu

118 Pascal's Triangle
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        lastLists = self.generate(numRows - 1)
        
        thisRow = [1] * numRows
        lastRow = lastLists[-1]
        
        for i in range(1, numRows-1, 1):
            thisRow[i] = lastRow[i - 1] + lastRow[i]
        
        return lastLists +[thisRow]
            
        
        
        

