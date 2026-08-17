# Given the head of a linked list, remove the nth node from the end of the list and return its head.




#Brute force solution  -Time complexity:O(n/2)  ,space complexity:O(1)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        if count==n:
            return head.next
        res=count-n
        cur=head
        for _ in range(res-1):
            cur=cur.next
        cur.next=cur.next.next
        return head
        


