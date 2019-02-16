# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:54:46 2018

@author: zhaoxu

807. Max Increase to Keep City Skyline
"""

import numpy as np

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s = 0
        l = len(grid)
        gridTrans = list(map(list, zip(*grid)))
        
        lef_rig = []
        top_bot = []
        
        
        for i in range(l):
            lef_rig.append( max(grid[i]))
            top_bot.append( max(gridTrans[i]))
            
        for r in range(l):
            rm = lef_rig[r]
            for c in range(l):
                newG = min(rm, top_bot[c])
                s += (newG - grid[r][c])
        return s
        
        
        """
        It seems that leetcode cannot use numpy???
        
        
        l = len(grid)
        #s = sum
        s = 0
        grid = np.array(grid)
        gridTrans = grid.transpose()
        
        top_bot = np.zeros(l)
        lef_rig = np.zeros(l)
        
        gridNew = np.zeros((l,l))
        
        for i in range(l):
            lef_rig[i] = grid[i].max()
            top_bot[i] = gridTrans[i].max()
            
        for r in range(l):
            rm = lef_rig[r]
            for c in range(l):
                gridNew[r][c] = min(rm, top_bot[c])
        
        s = sum(gridNew - grid)
        
        return int(s)
        
        """
        
        
        
        