# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:57:11 2018

@author: zhaoxu

226. Invert Binary Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        
        tmpT = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmpT)
        
        return root

