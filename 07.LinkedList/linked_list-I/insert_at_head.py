# Given the head of a singly linked list and an integer X, insert a node with value X at the head of the linked list and return 
# the head of the modified list.



#Time complexity :O(1) ,space complexity :O(1)
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next
    

class Solution:
    def insertAtHead(self, head, X):
        newnode=ListNode(X,head)
        return newnode 









