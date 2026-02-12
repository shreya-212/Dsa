# Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book,Allocate the books to m students 
# in such a way that the maximum number of pages assigned to a student is minimized. If the allocation 
# of books is not possible, return -1.




#Brute force solution   -Time complexity:O(n*(sum(nums)-max(nums))), space complexity:O(1)
class Solution:
    def findPages(self, nums, m):
        if m>len(nums):
            return -1
        def count_student(page):
            student=1
            count_page=0
            for num in nums:
                if count_page+num<=page:
                    count_page+=num
                else:
                    student+=1
                    count_page=num
            return student
                
        for page in range(max(nums),sum(nums)+1):
            student=count_student(page)
            if student<=m:
                return page
        return -1






#Optimal solution  -Time complexity:O(n*log(sum(nums))), space complexity:O(1)
class Solution:
    def findPages(self, nums, m):
        if m>len(nums):
            return -1
        def count_student(page):
            student=1
            count_page=0
            for num in nums:
                if count_page+num<=page:
                    count_page+=num
                else:
                    student+=1
                    count_page=num
            return student
                
        low,high=max(nums),sum(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            student=count_student(mid)
            if student<=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
