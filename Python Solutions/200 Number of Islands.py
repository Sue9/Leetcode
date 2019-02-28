# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:42:18 2019

@author: Sue

200. Number of Islands
"""

class Solution(object):
    def __init__(self):
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    def inArea(self, x, y, row, col):
        return (x >= 0) and (x < row) and (y >= 0) and (y < col)
        
    def dfs(self, grid, x, y, row, col, visited):
        visited[x][y] = True
        for d in self.dir:
            newX = x + d[0]
            newY = y + d[1]
            if(self.inArea(newX, newY, row, col)) and (not visited[newX][newY]) and (grid[newX][newY] == '1'):
                self.dfs(grid, newX, newY, row, col, visited)
        return
    
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if(row == 0) or (len(grid[0]) == 0):
            return 0
        col = len(grid[0])
        visited = [[False] * col for i in range(row)]
        
        res = 0
        
        for r in range(row):
            for c in range(col):
                if (not visited[r][c]) and (grid[r][c] == '1'):
                    res += 1
                    self.dfs(grid, r, c, row, col, visited)
        return res
