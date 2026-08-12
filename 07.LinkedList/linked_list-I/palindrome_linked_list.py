# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



#Brute force solution  -Time complexity:O(n) ,space complexity:O(n)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        left,right=0,len(arr)-1
        while left<right:
            if arr[left]!=arr[right]:
                return False
            left+=1
            right-=1
        return True






#Optimal solution  - Time complexity:O(n)  ,space complexity:o(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow
        prev=None
        current=head
        while current!=mid:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        left=prev
        right=mid.next if fast else mid
        while left and right:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True



        