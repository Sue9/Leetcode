# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:41:54 2019

@author: Sue

082. Remove Duplicates from Sorted List II
"""

import TEMPLATE4LinkedList as template

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head is None) or (head.next is None):
            return head
        
        m = head.val - 1
        dummy = template.ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while(cur and cur.next):
            if(cur.val == cur.next.val):
                m = cur.val
                cur = cur.next.next
                prev.next = cur
            elif(cur.val == m):
                cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        if(cur) and (cur.val == m):
            prev.next = cur.next
        
        return dummy.next
                
        
        
        
    


