# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.



#Brute force solution  -Time complexity:O(n+m)  ,space complexity:O(n+m)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        left=right=0
        merged=[]
        while left<len(nums1) and right<len(nums2):
            if nums1[left]<=nums2[right]:
                merged.append(nums1[left])
                left+=1
            else:
                merged.append(nums2[right])
                right+=1
        merged.extend(nums1[left:])
        merged.extend(nums2[right:])
        tot_len=len(nums1)+len(nums2)
        if tot_len%2==0:
            median=(merged[tot_len//2-1]+merged[tot_len//2])/2.0
        else:
            median=merged[tot_len//2]
        return median







#Optimal solution  -Time complexity:O(log(min(n,m)))  ,space complexity:O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        low,high=0,m
        while low<=high:
            cut1=(low+high)//2
            cut2=(m+n+1)//2-cut1
            leftA=nums1[cut1-1] if cut1>0 else float('-inf')
            rightA=nums1[cut1] if cut1<m else float('inf')
            leftB=nums2[cut2-1] if cut2>0 else float('-inf')
            rightB=nums2[cut2] if cut2<n else float('inf')

            if leftA<=rightB and leftB<=rightA:
                if (m+n)%2==0:
                    return (max(leftA,leftB)+min(rightA,rightB))/2.0
                else:
                    return max(leftA,leftB)
            elif leftA>rightB:
                high=cut1-1
            else:
                low=cut1+1



        
        