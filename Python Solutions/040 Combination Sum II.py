# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:14:05 2019

@author: Sue

40. Combination Sum II
"""

class Solution(object):
    def getCombinations(self, candidates, target, c, res):
        if target == 0:
            res.append(c[:])
            return
        
        if candidates == []:
            return
        
        distinctCandidates = list(set(candidates))
        
        # newCandidates != 0 & target != 0
        for i in range(len(distinctCandidates)):
            
            e = distinctCandidates[i]
            newTarget = target - e
            candidates.remove(e)
            
            newCandidates = list(filter(lambda x: x <= newTarget and x >= e, candidates))
            
            c.append(e)
            self.getCombinations(newCandidates, newTarget, c, res)
            c.pop()
            candidates.append(e)
            
        return
            
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if (candidates == []) or (target <= 0):
            return []
        
        # candidates != [] and target > 0
        
        res = list()
        c = list()
        self.getCombinations(candidates, target, c, res)
        return res
        