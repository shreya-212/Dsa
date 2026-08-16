# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, 
# and return the reordered list.



#Brute force solution   -time complexity:O(n)  ,space complexity:O(n)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        arr=[]
        cur=head
        while cur:
            arr.append(cur)
            cur=cur.next
        temp=ListNode(0)
        current=temp
        for i in range(0,len(arr),2):
            current.next=arr[i]
            current=current.next
        for i in range(1,len(arr),2):
            current.next=arr[i]
            current=current.next
        current.next=None
        return temp.next






#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head

            

            



        
        
        

    
        





        

            



        
        
        

    
        





        