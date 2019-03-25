# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:45:08 2019

@author: Sue

222. Count Complete Tree Nodes
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None):
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)