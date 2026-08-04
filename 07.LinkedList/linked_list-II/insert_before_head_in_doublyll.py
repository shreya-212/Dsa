# Given the head of a doubly linked list and an integer X, insert a node with value X before the head of the linked list and return 
# the head of the modified list.



# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        newnode=ListNode(X)
        if head is None:
            return newnode
        head.prev=newnode
        newnode.next=head
        return newnode