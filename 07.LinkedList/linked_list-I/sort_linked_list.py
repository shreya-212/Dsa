#Given the head of a linked list, return the list after sorting it in ascending order.



#Brute force solution -Time complexity:O(n log n)  ,space complexity:O(n)
class Solution(object):
    def sortList(self, head):
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        arr.sort()
        current=head
        for i in range(len(arr)):
            current.val=arr[i]
            current=current.next
        return head




#Optimal solution  -Time complexityO(n log n)  ,space complexity:O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def merge(self,l1,l2):
        new=ListNode()
        temp=new
        while l1 and l2:
            if l1.val<=l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        if l1:
            temp.next=l1
        else:
            temp.next=l2
        return new.next


    def sortList(self, head):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        right=slow.next
        slow.next=None
        left=head

        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
