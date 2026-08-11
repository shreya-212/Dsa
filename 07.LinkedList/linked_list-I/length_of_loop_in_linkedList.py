# Given the head of a singly linked list, find the length of the loop in the linked list if it exists. 
# Return the length of the loop if it exists; otherwise, return 0.




#Brute force solution  -Time complexity:O(n)  ,space complexity:O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        count=1
        node_check={}
        current=head
        while current:
            if current in node_check:
                value=node_check[current]
                return count-value
            node_check[current]=count
            count+=1
            current=current.next
        return 0






#Optimal solution  -Time complexity :O(n)  ,space complexity:O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        count=0
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                count=1
                current=slow.next
                while current!=slow:
                    current=current.next
                    count+=1
                return count
        return 0

                