class Solution:
     def twoSum(self, nums, target):
        prevMap={}
        for i,n in enumerate(nums):
            difference=target-n
            if difference in prevMap:
                return [prevMap[difference],i]
            prevMap[n]=i

        