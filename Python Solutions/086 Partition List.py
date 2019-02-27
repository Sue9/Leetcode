# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:13:23 2019

@author: Sue

086. Partition List
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def printListNode(self, head):
        s = ""
        while(head):
            s += str(head.val) + " -> "
            head = head.next
        s += "NULL"
        return s
        
    def createListNode(self, arr):
        if(arr == []):
            return ListNode(None)
        
        res = ListNode(arr[0])
        head = res
        for i in range(1, len(arr)):
            head.next = ListNode(arr[i])
            head = head.next
        return res
        
        
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if(head is None):
            return head
        
        ps = small = ListNode(0)
        pl = large = ListNode(0)
        
        while(head):
            if head.val < x:
                ps.next = head
                ps = ps.next
            else:
                pl.next = head
                pl = pl.next
            head = head.next
        pl.next = None
        ps.next = large.next
        return small.next
        """
        #first attempt
        
        if (head is None):
            return head
        
        smallPart = ListNode(None)
        largePart = ListNode(None)
        smallCur = smallPart
        largeCur = largePart
        
        while(head):
            print("\t\t")
            print("head is ", self.printListNode(head))
            cur = ListNode(head.val)
            head = head.next
            
            if(cur.val < x):
                smallCur.next = cur
                smallCur = smallCur.next
                print("smallPart is ", self.printListNode(smallPart))
                print("smallCur is ", self.printListNode(smallCur))
            else: #head.val >= x
                largeCur.next = cur
                largeCur = largeCur.next
                print("largePart is ", self.printListNode(largePart))
                print("largeCur is ", self.printListNode(largeCur))            
            
            print("\t\t")
        
        print("out WHILE")
        print("smallPart is ", self.printListNode(smallPart))
        print("smallCur is ", self.printListNode(smallCur))
        print("largePart is ", self.printListNode(largePart))
        print("largeCur is ", self.printListNode(largeCur))          
        smallCur.next = largePart.next
        print("smallPart = ", self.printListNode(smallPart))
        print("largePart = ", self.printListNode(largePart))
        
        return smallPart.next
        """