
class TwoSum:
    def twosum(self,nums,target):
        dict1 = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in dict1:
                return dict1[sub]
            else:
                dict1[nums[i]] = i


class Mergenums:
    def merge(self,nums1,m,nums2,n):
        for i in range(len(nums1)-1,-1,-1):
            if nums1[m-1] > nums2[n-1]:
                nums1[n+m-1] = nums1[m-1]
                m -= 1
            else:
                nums1[n+m-1] = nums2[n-1]
                n -= 1
        if n:
            nums1[:n] = nums2[:n]

class Removeduplicate:
    def removeduplicate(self,nums,val):
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
                continue
            index += 1
        return index

class RemoveSort:
    def removesort(self,nums,val):
        if not nums:return 0
        read = write = 1
        while read < len(nums):
            if nums[read] != nums[read-1]:
                write += 1
                nums[write] = nums[read]
            read += 1
        return write

class SearchElement:
    def search(self,nums,target):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] < target:
            return left + 1
        else:
            return left

class MaxSubarray:
    def maxsubarray(self,nums):
        if not nums:return 0
        maxsum_now = maxsum_tonow = 0
        for i in range(len(nums)):
            maxsum_now = max(nums[i],nums[i] + maxsum_now)
            maxsum_tonow = max(maxsum_tonow,maxsum_now)
        return maxsum_tonow

    def maxsubarray2(self,nums):
        for i in range(1,len(nums)):
            if nums[i-1] >0:
                nums[i] += nums[i-1]
        return max(nums)

class Numsadd1:
    def numsadd1(self,nums):
        tmp = ""
        for i in nums:
            tmp += str(nums[i])
        tmp_nums = int(tmp) + 1
        return [x for x in str(tmp_nums)]

    def numsadd12(self,nums):
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 9:
                nums[i] = 0
            else:
                nums[i] += 1
                break
        if nums[0] == 0:
            nums.insert(0,1)
        return nums










