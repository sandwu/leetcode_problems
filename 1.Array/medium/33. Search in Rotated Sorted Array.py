
class Solution(object):
    """
    不知道有没有和我一样的，想用最原始的方法来做，即先找出被颠倒的那个数，然后再用二分法分左右两次来求解
    虽然超时了，不过这个方法真是第一时间在脑海里浮现，由此看来，还得多练
    Runtime:time limit exceed
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0 
        end = len(nums)
        while start < end:
            mid = (start+end)/2
            if nums[mid] < nums[mid-1]:
                res = mid
                break
            elif nums[mid] > nums[start]:
                end = mid
            elif nums[mid] < nums[start]:
                start = mid
        if target > nums[0]:
            start = 0
            end = res
            while start < end:
                mid = (start+end)/2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid
                else:
                    end = mid
            return -1
        else:
            start = res
            end = len(nums)
            while start < end:
                mid = (start+end)/2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid
                else:
                    end = mid
            return -1


class Solution2(object):
    """
    讨论区的解法有两种，一种是利用二进制位运算求解，这次暂不研究，这边选取二分法，也是最容易浮现的解法
    在判断target>nums[0]时，一开始我的想法是只要判断target>nums[mid]就行了，结果出错，因为有两种情况，
    举例来说，target为4，一种是：4，5，0，1，2，此时因为中位数也就是0小于nums[0]，所以应该是end = mid-1
            另一种target为7，排列是：4，5，6，7，1，2，此时中位数也就是6大于nums[0],所以应该是start=mid+1
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Search in Rotated Sorted Array.
    Memory Usage: 10.8 MB, less than 93.14% of Python online submissions for Search in Rotated Sorted Array.
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0 
        end = len(nums)-1
        while start <= end:
            mid = (start+end)/2
            if target == nums[mid]:
                return mid
            if target >= nums[0]:
                if target > nums[mid] and nums[mid] >= nums[0]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target > nums[mid] or nums[mid] >= nums[0]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

