# Given head, the head of a linked list, determine if the linked list has a cycle in it.Return true if there is a cycle in the 
# linked list. Otherwise, return false.


#Brute force solution  -Time complexity:O(n)  ,space complexity:O(n)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        current=head
        node_check={}
        while current:
            if current in node_check:
                return True
            node_check[current]=1
            current=current.next
        return False


        
        




#Optimal solution  -Time complexity:O(n)  ,space complexity(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False


        
        