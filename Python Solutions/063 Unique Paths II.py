# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:31:04 2019

@author: Sue

63. Unique Paths II
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        if (row == 0):
            return 0
        
        col = len(obstacleGrid[0])
        
        memo = [[0] * col for i in range(row)]
        memo[0][0] = 1
        
        for i in range(row):
            for j in range(col):
                if(obstacleGrid[i][j] == 1):
                    memo[i][j] = 0
                    continue
                if(i == 0) and (j == 0):
                    continue
                
                if(i == 0):
                    memo[i][j] = memo[i][j-1]
                elif(j == 0):
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = memo[i][j-1] + memo[i-1][j]
        return memo[row-1][col-1]