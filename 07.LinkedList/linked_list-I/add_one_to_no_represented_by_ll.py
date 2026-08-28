# Given the head of a singly linked list representing a positive integer number.The task is to add one to the value
#  represented by the linked list and return the head of a linked list containing the final value.


#Time complexity:O(n)  ,space complexity:O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addOne(self, head):
        prev=None
        current=head
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        temp=prev
        carry=1
        while temp:
            temp.val+=carry
            if temp.val<10:
                carry=0
                break
            else:
                temp.val=0
                carry=1
            temp=temp.next
        if carry==1:
            new=ListNode(1)
            temp=prev
            while temp.next:
                temp=temp.next
            temp.next=new
        back=None
        cur=prev
        while cur:
            nxt=cur.next
            cur.next=back
            back=cur
            cur=nxt
        return back





