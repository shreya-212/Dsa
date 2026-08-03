# You are given the head of a singly linked list. Your task is to return the number of nodes in the linked list.




#Time complexity :O(n)   ,space complexity:O(1)
class Solution:
    def getLength(self, head):
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        return count