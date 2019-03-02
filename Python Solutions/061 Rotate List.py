# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:37:11 2019

@author: Sue

061. Rotate List
"""
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (k <= 0):
            return head
        
        if (head is None) or (head.next is None):
            return head
        
        size = 0
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while(cur):
            size += 1
            cur = cur.next
        
        # so that k <= size
        k = k % size
        if(k == 0):
            return head
        
        p = dummy
        q = p.next
        while(k > 1):
            q = q.next
            k -= 1
        
        # we have fix window p to q, then slide it to the end
        while(q.next):
            p = p.next
            q = q.next
        
        #q.next == NULL
        q.next = head
        newHead = p.next
        p.next = None
        
        return newHead
            
            
def printListNode(head):
    s = ""
    while(head):
        s += str(head.val) + " -> "
        head = head.next
    s += "NULL"
    return s
        
def createListNode(arr):
    if(arr == []):
        return ListNode(None)
        
    res = ListNode(arr[0])
    head = res
    for i in range(1, len(arr)):
        head.next = ListNode(arr[i])
        head = head.next
    return res
        
        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        