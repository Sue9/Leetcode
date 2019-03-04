# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:55:48 2019

@author: Sue

025. Reverse Nodes in k-Group
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
       
        
        
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (k <= 1):
            return head
        
        if (head is None):
            return head
        
        # k > 0 and head is not None
        p = dummy = ListNode(0)
        dummy.next = head 
                
        while(p.next):
            q = p.next
            
            for i in range(k-1):
                if q and q.next:
                    q = q.next
                else:
                    return dummy.next
            
            # reverse [p.next .. q]
            newQ = p.next
            newPNext = q.next
            prev = None
            cur = p.next
            
            for i in range(k):
                nextCur = cur.next
                cur.next = prev
                prev = cur
                cur = nextCur
            
            # link reversed k elements to the head
            newQ.next = newPNext
            
            p.next = prev
            p = newQ
            
        
        return dummy.next
            
        
            
            