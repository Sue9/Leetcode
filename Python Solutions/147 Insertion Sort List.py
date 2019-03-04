# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:24:02 2019

@author: Sue

147. Insertion Sort List
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def _insertionSortList(self, head, res):
        
        #head is not None
        while(head):
            cur = head
            head = head.next
            
            #insert cur into res
            p = q = ListNode(0)
            p.next = res
            
            while(p.next) and (cur.val > p.next.val):
                p = p.next
                
            # p.next is None
            # cur.val <= p.val
            cur.next = p.next
            p.next = cur
            res = q.next        
        return res          
        
        
        
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head is None) or (head.next is None):
            return head
        
        return self._insertionSortList(head, None)
        