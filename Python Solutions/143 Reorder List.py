# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:59:03 2019

@author: Sue

143. Reorder List
"""

class Solution(object):
    def reverseList(self, head):
        if (head is None) or (head.next is None):
            return head
        cur = head
        prev = None
        
        while(cur):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev
            
        
        
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if (head is None) or (head.next is None):
            return
        
        s = head
        size = 0
        while(s):
            size += 1
            s = s.next
        
        #find half
        dummyHalf = ListNode(0)
        dummyHalf.next = head
        h = int((size+1) / 2)
        while(h):
            dummyHalf = dummyHalf.next
            h -= 1
        half = dummyHalf.next
        dummyHalf.next = None
        
        #reverse tail
        revHalf = self.reverseList(half)
        
        #merge head and revHalf
        cur = head
        while(revHalf):
            temp = revHalf
            revHalf = temp.next
            temp.next = cur.next
            cur.next = temp
            cur = cur.next.next
        return

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
              