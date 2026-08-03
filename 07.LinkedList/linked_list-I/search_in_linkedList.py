# You are given the head of a singly linked list and an integer key.
# Return true if the key exists in the linked list, otherwise return false.



#Time complexity:O(n)  ,space complexity:O(1)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

        
class Solution:
    def searchKey(self, head, key):
        current=head
        while current:
            if current.val==key:
                return True
            current=current.next
        return False