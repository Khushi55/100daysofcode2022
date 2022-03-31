class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        u=len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                u=mid
            else:
                l=mid

        nums.insert(mid+1,target)
        nums.sort()
        print(nums)
        if nums[target]>mid:
             return mid+1
        else:
            return mid-1


nums=[2,3,5,6]
target=1

obj=Solution()
res=obj.searchInsert(nums,target)
print(res)
