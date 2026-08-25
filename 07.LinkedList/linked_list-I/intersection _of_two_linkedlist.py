# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two
# linked lists have no intersection at all, return null.




#Brute force solution  -Time complexity:O(n+m)  ,space complexity:O(n)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        check=set()
        temp1=headA
        temp2=headB
        while temp1:
            check.add(temp1)
            temp1=temp1.next
        while temp2:
            if temp2 in check:
                return temp2
            temp2=temp2.next
        return None



        
        
        

        
        
        