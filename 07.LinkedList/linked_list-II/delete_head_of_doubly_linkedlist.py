# Given the head of a doubly linked list, remove the node at the head of the linked list and return the head of the modified list.
# The head is the first node of the linked list.




class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        head=head.next
        head.prev=None
        return head
    
        
        
        
        