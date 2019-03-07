# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:46:53 2019

@author: Sue

62. Unique Paths
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: col: int
        :type n: row: int
        :rtype: int
        """
        if (m <= 0) or (n <= 0):
            return 0
        
        if (m == 1) or (n == 1):
            return 1
        
        #memo[i][j] = memo[i-1][j] + memo[i][j-1]
        memo = [[0] * m for i in range(n)]
        memo[0][0] =  1
        for i in range(n):
            for j in range(m):
                if(i == 0) and (j == 0):
                    continue
                
                if(i == 0):
                    memo[i][j] = memo[i][j-1]
                elif(j == 0):
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
                #print("i = ", i, " j =", j)
                #print("memo = ", memo)
                
        return memo[n-1][m-1]
                
                
        