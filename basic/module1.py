class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        u = len(nums) - 1
        while l <= u:
            mid = (l + u) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                u = mid - 1
            else:
                l = mid + 1

        nums.append(target)
        nums.sort()

        a=nums.index(target)
        return a



nums = [1, 3, 5, 6]
target =7

obj = Solution()
res = obj.searchInsert(nums, target)
print(res)
