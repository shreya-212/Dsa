#You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.


#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def deleteMiddle(self, head):
        slow=fast=head
        fast=fast.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
