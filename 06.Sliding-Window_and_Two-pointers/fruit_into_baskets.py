# There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees,
# where fruits[i] denotes the kind of fruit produced by the ith tree.Return the maximum number of fruits that can be picked.





#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(n)
class Solution:
    def totalFruits(self, fruits):
        max_fruits=0
        for i in range(len(fruits)):
            types=set()
            for j in range(i,len(fruits)):
                types.add(fruits[j])
                if len(types)>2:
                    break
                max_fruits=max(max_fruits,j-i+1)
        return max_fruits





#Optimal solution   =Time complexity:O(n)  ,space complement :O(n)
class Solution:
    def totalFruits(self, fruits):
        max_fruits=0
        types={}
        left=0
        for right in range(len(fruits)):
            types[fruits[right]]=types.get(fruits[right],0)+1
            while len(types)>2:
                types[fruits[left]]-=1
                if types[fruits[left]]==0:
                    del types[fruits[left]]
                left+=1
            max_fruits=max(max_fruits,right-left+1)
        return max_fruits

    

