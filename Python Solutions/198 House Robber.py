# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:31:45 2018

@author: Sue

198 House Robber
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #iterative + 2 variables
        if(len(nums) == 0):
            return 0
        prev1 = prev2 = 0
        for n in nums:
            tmp = prev1
            prev1 = max(n+prev2, prev1)
            prev2 = tmp
        return prev1
        
        """
        #iterative + memo
        n = len(nums)
        if(n == 0):
            return 0
        if(n == 1):
            return nums[0]
        
        memo = [-1] * (n)
        memo[0] = nums[0]
        
        for i in range(1, n):
            if (i < 2):
                memo[i] = max(nums[i], memo[i-1])
            else:
                memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return memo[n-1]
        """
        
        """
        #memo[i]: stores maximum amount of money we can rob from i to the last house
        #which is [i..n]
        n = len(nums)
        if(n == 0):
            return 0
        if(n == 1):
            return nums[0]
        if(n == 2):
            return max(nums)
        
        memo = [-1] * (n)
        memo[n-1] = nums[n-1]
        
        
        for i in range(n-2, -1, -1):
            for j in range(i, n):
                if (j+2) <= (n-1):
                    memo[i] = max(memo[i], nums[j] + memo[j+2])
                else:
                    memo[i] = max(memo[i], nums[j])
        
        
        return memo[0]
        """
        
        