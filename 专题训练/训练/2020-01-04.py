
def isBadversion(x):
    pass


class Solution:
    def first_badversion(self,n):
        left = 0
        right = n
        while left<=right:
            mid = (left+right) >> 1
            if isBadversion(mid):
                if isBadversion(mid-1):
                    right = mid - 1
                else:
                    return mid
            else:
                if isBadversion(mid + 1):
                    return mid+1
                else:
                    left = mid + 1