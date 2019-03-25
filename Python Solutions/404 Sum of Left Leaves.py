# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:14:03 2019

@author: Sue

404. Sum of Left Leaves
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None) :
            return 0
        
        if (root.left is None):
            return self.sumOfLeftLeaves(root.right)
        
        if (root.left.left is None) and (root.left.right is None):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        