# Given the head of a singly linked list consisting of only 0, 1 or 2.
# Sort the given linked list and return the head of the modified list.



#Brute force solution  -Time complexity:O(n)  ,space complexity:O(1)
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def sortList(self, head):
        current=head
        count0=count1=count2=0
        while current:
            if current.data==0:
                count0+=1
            elif current.data==1:
                count1+=1
            else:
                count2+=1
            current=current.next
        current=head
        while current:
            if count0:
                current.data=0
                count0-=1
            elif count1:
                current.data=1
                count1-=1
            else:
                current.data=2
                count2-=1
            current=current.next
        return head

        