class Solution(object):


        def firstBadVersion(self, n):

            l = 1
            u = n
            while l < u:
                mid = (l + u) // 2
                if isBadversion(mid):
                    u= mid

                else:
                    l = mid + 1
            return l

n=5
obj=Solution()
res=obj.firstBadVersion(n)
print(res)
