# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit.Add the two numbers and return the sum as a linked list.





#Time complexity:O(max(m,n))  space complexity:O(max(m,n))
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode()
        temp=dummy
        carry=0
        while (l1 or l2)or carry:
            sum_val=0
            if l1 :
                sum_val+=l1.val
                l1=l1.next
            if l2:
                sum_val+=l2.val
                l2=l2.next
            sum_val+=carry
            carry=sum_val//10
            new=ListNode(sum_val%10)
            temp.next=new
            temp=temp.next
        return dummy.next
        
        




        