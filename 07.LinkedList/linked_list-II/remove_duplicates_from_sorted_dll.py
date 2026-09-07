# Given the head of a doubly linked list with its values sorted in non-decreasing order. Remove all duplicate occurrences 
# of any value in the list so that only distinct values are present in the list.
# Return the head of the modified linked list.


#Time complexity:  O(n)  ,space complexity:O(1)
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        cur=head
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
                if cur.next:
                    cur.next.prev=cur
            else:
                cur=cur.next
        return head


        