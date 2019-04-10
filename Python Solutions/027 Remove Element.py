# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:15:49 2019

@author: Sue

027. Remove Element
"""
class Solution:
    #def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val) -> int:
        k = 0
        for i in range(len(nums)):
            
            if(nums[i] != val):
                if(k != i):
                    
                    #swap nums[i] and nums[k]
                    temp = nums[i]
                    nums[i] = nums[k]
                    nums[k] = temp
                k += 1
                    
            print("\t")
        return k
                
        