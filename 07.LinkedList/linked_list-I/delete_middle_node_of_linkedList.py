#You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.



#Brute force solution -Time complexity:O(n)  space complexity:O(1)
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        mid=count/2
        cur=head
        for _ in range(mid-1):
            cur=cur.next
        cur.next=cur.next.next
        return head






#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow=fast=head
        fast=fast.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
