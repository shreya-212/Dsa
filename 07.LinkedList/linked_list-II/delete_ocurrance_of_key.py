# Given the head of a doubly linked list and an integer target. Delete all nodes in the linked list with the value target
#  and return the head of the modified linked list.


#Time complexity:O(n)  ,space complexity:O(1)
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        cur=head
        while cur:
            nxt=cur.next
            if cur.val==target:
                if cur.prev:
                    cur.prev.next=cur.next
                else:
                    head=cur.next
                if cur.next:
                    cur.next.prev=cur.prev
            cur=nxt
        return head

            


