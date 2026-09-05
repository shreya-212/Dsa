# Given the head of a sorted doubly linked list of positive distinct integers, and a target integer, return a 2D array containing all 
# unique pairs of nodes (a, b) such that a + b == target.



#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(1)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, head, target):
        temp=head
        l=[]
        while temp:
            temp2=temp.next
            while (temp2 is not None  and  temp.val+temp2.val<=target):
                if temp.val+temp2.val==target:
                    l.append([temp.val,temp2.val])
                temp2=temp2.next
            temp=temp.next
        return l

