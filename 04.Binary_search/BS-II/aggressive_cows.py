# Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, 
# assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. 
# Find the maximum possible minimum distance.


#Brute force solution  -Time complexity:O(n log n +n * max_dist) ,space complexity:O(1)
class Solution:
    def aggressiveCows(self, nums, k):
        def can_place(nums,dist,k):
            count_cow=1
            last=nums[0]
            for i in range(1,len(nums)):
                if nums[i]-last>=dist:
                    count_cow+=1
                    last=nums[i]
                    if count_cow>=k:
                        return True
            return False

        nums.sort()
        max_dist=max(nums)-min(nums)
        for dist in range(1,max_dist+1):
            if can_place(nums,dist,k):
                continue
            else:
                return dist-1
        return max_dist


       

            

#Optimal solution  -Time complexity:O(n log n+ n*log(max_dist)),space complexity:O(1)
class Solution:
    def aggressiveCows(self, nums, k):
        def can_place(nums,dist,k):
            count_cow=1
            last=nums[0]
            for i in range(1,len(nums)):
                if nums[i]-last>=dist:
                    count_cow+=1
                    last=nums[i]
                    if count_cow>=k:
                        return True
            return False

        nums.sort()
        max_dist=nums[-1]-nums[0]
        low,high=1,max_dist
        ans=0
        while low<=high:
            mid=(low+high)//2
            if can_place(nums,mid,k):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
            

       

            


        

            


        