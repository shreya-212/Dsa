# Given the head of a linked list, remove the nth node from the end of the list and return its head.




#Brute force solution  -Time complexity:O(n/2)  ,space complexity:O(1)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        if count==n:
            return head.next
        res=count-n
        cur=head
        for _ in range(res-1):
            cur=cur.next
        cur.next=cur.next.next
        return head
        



#Optimal solution time complxity;O(n),space complexity:O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=ListNode(0,head)
        slow=fast=temp
        for i in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return temp.next
        
        
