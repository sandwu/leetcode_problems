


class Solution:
    def plusone(self,nums): #判断当前是否为9即可
        if not nums:return
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 9:
                nums[i] = 0
            else:
                nums[i] += 1
                break
        if nums[0] == 1:
            nums.insert(0,1)
        return nums


    def plusone2(self,nums):
        if not nums:return
        tmp = ""
        for i in nums:
            tmp += str(i)
        tmp_nums = int(tmp) + 1
        return [int(i) for i in str(tmp_nums)]
