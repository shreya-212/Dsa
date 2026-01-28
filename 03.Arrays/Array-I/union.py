# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays.
# The elements in the union must be in ascending order.



#Brute force Solution- Time complexity:O((n1+n2)log(n1+n2)), space complexity:O(n1+n2)
class Solution:
    def unionArray(self, nums1, nums2):
        u=set()
        for i in range(len(nums1)):
            u.add(nums1[i])
        for i in range(len(nums2)):
            u.add(nums2[i])
        result=list(u)
        result.sort()
        return result







#Optimal solution-Time complexity:O(n1+n2),space complexity:O(n1+n2)
class Solution:
    def unionArray(self, nums1, nums2):
        result=[]
        i=j=0
        while i <len(nums1) and j <len(nums2):
            if nums1[i]<nums2[j]:
                if not result or result[-1]!=nums1[i]:
                    result.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                if not result or result[-1]!=nums2[j]:
                    result.append(nums2[j])
                j+=1
            else:
                if not result or result[-1]!=nums1[i]:
                    result.append(nums1[i])
                i+=1
                j+=1
        while i<len(nums1):
                if not result or result[-1]!=nums1[i]:
                    result.append(nums1[i])
                i+=1
        while j<len(nums2):
                if not result or result[-1]!=nums2[j]:
                    result.append(nums2[j])
                j+=1
        return result