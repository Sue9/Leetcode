# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:45:06 2019

@author: Sue

437. Path Sum III
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        