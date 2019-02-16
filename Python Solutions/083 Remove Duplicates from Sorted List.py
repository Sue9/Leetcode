# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:59:38 2019

@author: Sue

83. Remove Duplicates from Sorted List
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(None)
        prev.next = head
        p = prev
        
        e = p.val
        while(p.next):
            if(p.next.val == e):
                #delete p.next
                p.next = p.next.next
            else:
                e = p.next.val
                p = p.next
        
        return prev.next
        