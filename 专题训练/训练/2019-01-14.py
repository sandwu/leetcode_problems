



class Solution:
    def isbst(self,root):
        res = []
        self.inorder(root,res)
        return res

    def inorder(self,root,res):
        if not root:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)

    #[10,9,2,5,3,7,101,18] 4
    def longestnum(self,nums):
        if not nums: return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


nums = [10,9,2,5,3,7,101,18]
s = Solution()
print(s.longestnum(nums))