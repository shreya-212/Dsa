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






#Optimal solution  - Time complexity:O(n)  ,space complexity:O(1)
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
        cur=slow
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        left=head
        right=prev
        while left and right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True








        