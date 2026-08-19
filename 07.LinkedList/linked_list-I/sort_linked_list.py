#Given the head of a linked list, return the list after sorting it in ascending order.




#Brute force solution -Time complexity:O(log n)  ,space complexity:O(n)
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
