# Given the head of a singly linked list, reverse the list, and return the reversed list.



#Brute force solution  -Time complexity:O(n) ,space complexiy:O(n)
class Solution(object):
    def reverseList(self, head):
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        current=head
        for value in reversed(arr):
            current.val=value
            current=current.next
        return head






#Optimal solution  -Time complexity:O(n) ,space complexity:O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        current=head
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        return prev
