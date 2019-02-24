# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 09:54:06 2019

@author: Sue

39. Combination Sum
"""

class Solution(object):
    def findCombinations(self, candidates, target, c, res):
        """
        :type candidates: List[int]
        :type target: int
        :type c: List[int] : current combination result
        :type res: List[List[int]] : result
        :rtype: void
        """
        if (target == 0):
            res.append(c[:])
            return
        # target != 0
        if (candidates == []):
            return
        
        # target != 0 & candidates != []
        # do recursion
        for i in range(len(candidates)):
            e = candidates[i]
            newTarget = target - e
            newCandidates = list(filter(lambda x : x >= e and x <= newTarget, candidates))
            
            c.append(e)
            self.findCombinations(newCandidates, newTarget, c, res)
            c.pop()
        return
            
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if (candidates == []) or (target <= 0):
            return []
        
        #cadidates is not empty & target > 0
        #filter candidates that each element <= target
        res = list()
        c = list()
        newCandidates = list(filter(lambda x: x >= 0 and x <= target, candidates))
        self.findCombinations(newCandidates, target, c, res)
        return res
        