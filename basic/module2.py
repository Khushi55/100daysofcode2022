from math import pow
class Solution(object):
    def sortedSquares(self, nums):


       + for i in len(nums):
            nums[i]*=nums[i]


        a=nums.sort()
        return a






nums=[-4,-1,0,3,10]
obj=Solution()
res=obj.sortedSquares(nums)
print(res)
