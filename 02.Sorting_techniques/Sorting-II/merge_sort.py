# Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm.
#  Return the sorted array.

def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left=mergeSort(nums[:mid])
    right=mergeSort(nums[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

