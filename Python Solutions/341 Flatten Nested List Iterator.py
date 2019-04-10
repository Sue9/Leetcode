# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:30:15 2019

@author: Sue

341. Flatten Nested List Iterator
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nl = nestedList
        self.l = []
        
        
        self.dummy = -1
        self.start = 0
        self.end = len(nestedList) - 1
        
        

    def next(self):
        """
        :rtype: int
        """
        nextIndex = self.dummy + 1
        
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        nextIndex = self.dummy + 1
        #reach the last element
        if (nextIndex == self.end):
            return False
        else:
            return True
        
    def g

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())