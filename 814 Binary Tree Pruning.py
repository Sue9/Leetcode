# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:42:41 2019

@author: Sue

814. Binary Tree Pruning
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution(object):
    def hasOne(self, root):
        """
        :type root: TreeNode
        :rtype: Boolean
        """
        if (root is None):
            return False
        
        if (root.val == 1):
            return True
        
        return self.hasOne(root.left) or self.hasOne(root.right)
    
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if (root is None):
            return root
        
        if (self.hasOne(root.left)):
            root.left = self.pruneTree(root.left)
        else:
            root.left = None
        
        if (self.hasOne(root.right)):
            root.right = self.pruneTree(root.right)
        else:
            root.right = None
            
        return root