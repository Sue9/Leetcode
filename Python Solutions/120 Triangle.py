# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:41:04 2019

@author: Sue

120. Triangle
"""

class Solution(object):
    def inArea(self, x, y, row):
        """
        :type x: int : x-coordinate
        :type y: int : y-coordinate
        :type row: int : total row numbers
        :rtype: bool
        """
        return (x >= 0) and (x < row) and (y >= 0) and (y <= x)
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #from bottom to up
        if(len(triangle) == 0) or (len(triangle[0]) == 0):
            return 0
        
        minTriangle = []
        minTriangle.append(triangle[0])
        shift = [[-1, -1], [-1, 0]]
        row = len(triangle)
        
        for r in range(1, row):
            minRes = []
            for c in range(r+1):
                validPath = []
                for d in shift:
                    newX = r + d[0]
                    newY = c + d[1]
                    if self.inArea(newX, newY, row):
                        validPath.append(minTriangle[newX][newY])
                    
                #minTriangle[r][c] = triangle[r][c] + min(validPath)
                minRes.append(triangle[r][c] + min(validPath))
            minTriangle.append(minRes)
        
        return min(minTriangle[row-1])
        
        