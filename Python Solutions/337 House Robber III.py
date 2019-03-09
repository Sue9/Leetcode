# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:00:02 2019

@author: Sue

337. House Robber III
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):        
    def robHelper(self, root, dictRoot):
        if (root is None):
            return 0
        
        if (dictRoot.__contains__(root)):
            return dictRoot[root]
        
        val = 0
        if (root.left):
            val += self.robHelper(root.left.left, dictRoot) + self.robHelper(root.left.right, dictRoot)
        
        if (root.right):
            val += self.robHelper(root.right.left, dictRoot) + self.robHelper(root.right.right, dictRoot)
        val = max(val + root.val, self.robHelper(root.left, dictRoot) + self.robHelper(root.right, dictRoot))
        dictRoot[root] = val
        return val
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #update root
        if(root is None):
            return 0
        
        dictRoot = {}
        return self.robHelper(root, dictRoot)
        
        
        """
        #Fail: Time Limit Exceed
        #recursion way
        if (root is None):
            return 0
        
        
        option1 = root.val
        if (root.left):
            option1 = option1 + self.rob(root.left.left) + self.rob(root.left.right)
        
        if (root.right):
            option1 = option1 + self.rob(root.right.left) + self.rob(root.right.right)
        
        option2 = self.rob(root.left) + self.rob(root.right)
        
        return max(option1, option2)
        """