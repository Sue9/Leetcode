# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:55:48 2019

@author: Sue

025. Reverse Nodes in k-Group
"""
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
        print("===================================================")
        print("p is", printListNode(p))
        print("dummy is", printListNode(dummy))
        print("\t\t")
        
        while(p.next):
            q = p.next
            print("---------------")
            print("q is", printListNode(q))
            for i in range(k-1):
                if q and q.next:
                    q = q.next
                else:
                    print("RETURN!!!")
                    return dummy.next
            print("q is", printListNode(q))
            # reverse [p.next .. q]
            newQ = p.next
            newPNext = q.next
            prev = None
            cur = p.next
            print("Before reverse:")
            print("newQ is", printListNode(newQ))
            print("newPNext is", printListNode(newPNext))
            for i in range(k):
                nextCur = cur.next
                cur.next = prev
                prev = cur
                cur = nextCur
            print("\t\t")
            print("After reverse:")
            print("cur is", printListNode(cur))
            print("prev is", printListNode(prev))
            # link reversed k elements to the head
            newQ.next = newPNext
            print("newQ is", printListNode(newQ))
            p.next = prev
            p = newQ
            #head = dummy.next
            print("p is", printListNode(p))
            print("dummy is", printListNode(dummy))
            print("-----------------")
        #head = dummy.next
        return dummy.next
            
        
            
            