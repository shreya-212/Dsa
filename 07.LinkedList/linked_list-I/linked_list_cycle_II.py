# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.



#Brute force solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def detectCycle(self, head):
        node_check={}
        current=head
        while current:
            if current in node_check:
                return current
            node_check[current]=1
            current=current.next
        return None





#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def detectCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None