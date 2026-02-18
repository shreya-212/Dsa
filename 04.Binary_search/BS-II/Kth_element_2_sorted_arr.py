# Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.


#Brute force solution   -Time complexity:O(k)  ,space complexity:O(n)
class Solution:
    def kthElement(self, a, b, k):
        left=right=0
        count=0
        while left<len(a) and right<len(b):
            if a[left]<b[right]:
                num=a[left]
                left+=1
            else:
                num=b[right]
                right+=1
            count+=1
            if count==k:
                return num
        while left<len(a):
            num=a[left]
            count+=1
            if count==k:
                return num
            left+=1
        while right<len(b):
            num=b[right]
            count+=1
            if count==k:
                return num
            right+=1
        


    
            


#Optimal solution  -Time complexity:O(log(min(m,n)))  ,space complexity:O(1)
class Solution:
    def kthElement(self, a, b, k):
        if len(a)>len(b):
            a,b=b,a
        m=len(a)
        n=len(b)
        low,high=max(0,k-n),min(k,m)
        while low<=high:
            partA=(low+high)//2
            partB=k-partA
            leftA=a[partA-1] if partA>0 else float('-inf')
            rightA=a[partA] if partA<m else float('inf')
            leftB=b[partB-1] if partB>0 else float('-inf')
            rightB=b[partB] if partB<n else float('inf')
            if leftA<=rightB and leftB<=rightA:
                return max(leftA,leftB)
            elif leftA>rightB:
                high=partA-1
            else:
                low=partA+1
            