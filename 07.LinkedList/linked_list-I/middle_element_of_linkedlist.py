# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


#Brute force solution  -Time complexity:O(n) ,space complexity:O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        mid=count//2+1
        current=head
        while current:
            mid-=1
            if mid==0:
                break
            current=current.next
        return current





#Optimal Solution  -Time complexity:O(n)  ,space complexity:O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    