# Given the head of a singly linked list, delete the head of the linked list and return the head of the modified list.
# The head is the first node of the linked list.


#Time complexity:O(1) , space complexity:O(1)
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def deleteHead(self, head):
        if head is None :
            return None
        return head.next
        