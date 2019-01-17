# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 10:32:23 2019

@author: Sue

965 Univalued Binary Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        

class Solution(object):
    def isUnivalTreeHelper(self, root, val):
        """
        :type root: TreeNode
        :type val: Int
        :rtype: bool
        """
        if(root is None):
            return True
        
        if(root.val == val):
            return self.isUnivalTreeHelper(root.right, val) and self.isUnivalTreeHelper(root.left, val)
        
        return False
        
        
        
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root is None):
            return True
        
        return self.isUnivalTreeHelper(root.right, root.val) and self.isUnivalTreeHelper(root.left, root.val)
        
        