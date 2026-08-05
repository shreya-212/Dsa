# You are given the head of a doubly linked list.
# Reverse the list in-place and return the new head of the reversed list.





#Time complexity:O(n)  ,space complexity:O(1)
class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def reverseDLL(self, head):
        current=head
        last_node=None
        while current:
            current.next,current.prev=current.prev,current.next
            last_node=current
            current=current.prev
        return last_node
