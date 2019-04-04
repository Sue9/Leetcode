# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:55:07 2019

@author: Sue

102. Binary Tree Level Order Traversal
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        
        if (root is None):
            return res
        
        
        q = Queue()
        q.put((0, root))
        
        while (not q.empty()):
            top = q.get()
            curLevel = top[0]
            #new level
            if curLevel >= len(res):
                res.append([top[1].val])
            else:
                res[curLevel].append(top[1].val)
            
            if (top[1].left):
                q.put((curLevel+1,top[1].left))
            if (top[1].right):
                q.put((curLevel+1,top[1].right))
            print(res)
        
        return res
            
            