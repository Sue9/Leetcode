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
    def getAllNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List(Int)
        """
       
        if not root:
            return []
        
        return [root.val] + self.getAllNodes(root.left) + self.getAllNodes(root.right)
        
        
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        nodes = self.getAllNodes(self, root)
        