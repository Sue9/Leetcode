# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:48:19 2018

@author: zhaoxu

654 Maximum Binanry Tree
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
#        if len(nums) == 2:
#            if nums[0] > nums[1]:
#                t = TreeNode(nums[0])
#                t.right = TreeNode(nums[1])
#            else:
#                t = TreeNode(nums[1])
#                t.left = TreeNode(nums[0])
#            return t
        
        t = TreeNode(max(nums))
        ind = nums.index(max(nums))
        t.left = self.constructMaximumBinaryTree(nums[0:ind])
        t.right = self.constructMaximumBinaryTree(nums[ind+1:])
        
        return t
        
            