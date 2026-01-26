# Given an integer array nums. Return the number of inversions in the array.
# Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.





#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(1)
class Solution:
    def numberOfInversions(self, nums):
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    count+=1
        return count
    









#Optimal Solution   -Time complexity:O(n log n)  ,space complexity:O(n)
class Solution:
    def numberOfInversions(self, nums):
        def merge(arr):
            if len(arr)<=1:
                return arr,0
            mid=len(arr)//2
            left,left_count=merge(arr[:mid])
            right,right_count=merge(arr[mid:])
            merged=[]
            i=j=count=0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    count+=len(left)-i
                    j+=1
            while i<len(left):
                merged.append(left[i])
                i+=1
            while j<len(right):
                merged.append(right[j])
                j+=1
            return merged,left_count+right_count+count

        sorted_arr,inversion_count=merge(nums)
        return inversion_count
        
       
        

            
            



        