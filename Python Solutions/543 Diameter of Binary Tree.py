# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:13:00 2018

@author: zhaoxu


543 Diameter of Binary Tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
        
class Solution(object):
    
    
    
    def maxLenOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        return  1 + max(self.maxLenOfBinaryTree(root.left), self.maxLenOfBinaryTree(root.right))
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        longestPath = 0
        
        longestPath = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        return max(longestPath, self.maxLenOfBinaryTree(root.left) + self.maxLenOfBinaryTree(root.right))
        
    
    
    
    """
    #Fail: wrong answer
    
    
    def diameterOfBinaryTree(self, root):
        
        
        if root is None:
            return 0
        
        if root.left is not None and root.right is None:
#            return max(1 + self.maxLenOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            return self.maxLenOfBinaryTree(root.left)
        
        if root.left is None and root.right is not None:
            return self.maxLenOfBinaryTree(root.right)
        
        return self.maxLenOfBinaryTree(root.left) + self.maxLenOfBinaryTree(root.right)
    
    
    """
        