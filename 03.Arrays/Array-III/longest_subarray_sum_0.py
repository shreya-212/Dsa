# You are given an integer array arr of size n which contains both positive and negative integers. 
# Your task is to find the length of the longest contiguous subarray with sum equal to 0.


#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(1)
class Solution:
    def maxLen(self, arr):
        n=len(arr)
        max_len=0
        for i in range(n):
            subsum=0
            length=0
            for j in range(i,n):
                subsum+=arr[j]
                if subsum==0:
                    length=j-i+1
                    max_len=max(max_len,length)
        return max_len
    






#Optimal solution  -Time complexity:O(n) ,space complexity:O(n)
class Solution:
    def maxLen(self, arr):
        n=len(arr)
        prefix={0:-1}
        subsum=0
        max_len=0
        for i in range(n):
            subsum+=arr[i]
            if subsum in prefix:
                max_len=max(max_len,i-prefix[subsum])
            else:
                prefix[subsum]=i
        return max_len
