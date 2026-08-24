# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two
# linked lists have no intersection at all, return null.




#Brute force solution  -Time complexity:O(n*m)  ,space complexity:O(n)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        seen={}
        temp1=headA
        temp2=headB
        while temp1:
            seen[temp1]=seen.get(temp1,0)+1
            temp1=temp1.next
        while temp2:
            if temp2 in seen:
                return temp2
            temp2=temp2.next
        return None

        
        
        