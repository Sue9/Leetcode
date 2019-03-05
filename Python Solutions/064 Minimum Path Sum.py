# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:53:36 2019

@author: Sue

064. Minimum Path Sum
"""

class Solution(object):
    def inArea(self, x, y, row, col):
        return (x >= 0) and (x < row) and (y >= 0) and (y < col)
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if (len(grid) == 0) or (len(grid[0]) == 0):
            return 0
        
        m = len(grid)
        n = len(grid[0])
        dir =[[-1, 0], [0, -1]]
        
        
        for r in range(m):
            for c in range(n):
                
                if r == 0 and c == 0:
                    continue
                fromPathMin = []
                for d in dir:
                    lastR = r + d[0]
                    lastC = c + d[1]
                    if self.inArea(lastR, lastC, m, n):
                        fromPathMin.append(grid[lastR][lastC])
                
                grid[r][c] += min(fromPathMin)
                
        return grid[m-1][n-1]
        
        