# Given the head of a sorted doubly linked list of positive distinct integers, and a target integer, return a 2D array containing all 
# unique pairs of nodes (a, b) such that a + b == target.



#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(n)
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




#Optimal solution  -Time complexity:O(n)  ,space ciomplexity:O(n)
class Solution:
    def findPairsWithGivenSum(self, head, target):
        left=head
        right=head
        while right and right.next:
            right=right.next
        result=[]
        while left and right and left!=right and left.prev!=right:
            cur_sum=left.val+right.val
            if cur_sum==target:
                result.append([left.val,right.val])
                left=left.next
                right=right.prev
            elif cur_sum<target:
                left=left.next
            else:
                right=right.prev
        return result