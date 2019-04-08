# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:59:03 2019

@author: Sue

103. Binary Tree Zigzag Level Order Traversal
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) :#-> List[List[int]]:
        if (root is None):
            return []
        
        res = []
        q = Queue()
        #(level, direction, tree)
        #true : left to right
        #false: right to left
        q.put((0, True, root))
        while (not q.empty()):
            top = q.get()
            level = top[0]
            leftToRight = top[1]
            node = top[2]
            if(level >= len(res)):
                res.append([node.val])
            else:
                #res[level] has existed
                if leftToRight:
                    res[level].append(node.val)
                else:
                    res[level] = [node.val] + res[level]
                    
            
            if (node.left):
                q.put((level+1, not leftToRight, node.left))
            if (node.right):
                q.put((level+1, not leftToRight, node.right))
        return res
        