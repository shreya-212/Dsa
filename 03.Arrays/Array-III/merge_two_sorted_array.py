# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.





#Brute force solution -Time complexity:O(m+n)  ,space complexity:O(m+n)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left=right=0
        result=[]
        while left<m and right <n:
            if nums1[left] <nums2[right]:
                result.append(nums1[left])
                left+=1
            else:
                result.append(nums2[right])
                right+=1
        while left<m:
            result.append(nums1[left])
            left+=1
        while right<n:
            result.append(nums2[right])
            right+=1
        nums1[:]=result
        









#Optimal Solution -Time complexity:O(m+n) ,space complexity:O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=m-1
        k=m+n-1
        j=n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                k-=1
                i-=1
            else:
                nums1[k]=nums2[j]
                k-=1
                j-=1
        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1
        return nums1


        
        