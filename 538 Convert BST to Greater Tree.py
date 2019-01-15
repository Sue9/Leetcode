# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:13:07 2018

@author: Sue

538 Convert BST to Greater Tree

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
        
class Solution(object):     
        
    def inOrder(self, root, s):
        """
        :type root: TreeNode
        :type s: Int
        :rtype: Int
        """
        if(root is None):
            return s
        
        s = self.inOrder(root.right, s)
        
        s += root.val
        root.val = s
        
        s = self.inOrder(root.left, s)
        
        return s
        
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        s = self.inOrder(root, 0)
        
        return root
        