# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:37:38 2019

@author: Sue

145. Binary Tree Postorder Traversal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        
        if(root is None):
            return res
        
        stack = [['go', root]] + stack
        print(stack)
        while stack:
            top = stack[0]
            stack = stack[1:]
            if (top[0] == "print"):
                res.append(top[1].val)
            
            if (top[0] == "go"):
                stack = [["print", top[1]]] + stack
                if (top[1].right):
                    stack = [["go", top[1].right]] + stack
                if (top[1].left):
                    stack = [["go", top[1].left]] + stack
            print("\t")
            print(stack)
            print("\t")
        return res
                