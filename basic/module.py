from math import pow
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        u=len(nums)-1
        while l<=u:
            a=nums[l]
            b=a*a
            c=[b]
            l=l+1
            print (c)
        d=c.sort()
        print(d)










nums=[-4,-1,0,3,10]
obj=Solution()
res=obj.sortedSquares(nums)
print(res)
