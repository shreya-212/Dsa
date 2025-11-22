#Reverse an array
class Solution:
    def reverse(self, arr,start,end):
        if start>end:
            return
        arr[start],arr[end]=arr[end],arr[start]
        return self.reverse(arr,start+1,end-1)
        


s=Solution()
arr=[1,2,3,4,5]
s.reverse(arr,0,len(arr)-1)
print(arr)