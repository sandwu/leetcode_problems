
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

    def longest_increasing_subsequence(self,nums):
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1,len(nums)):
            tmax = 1
            for j in range(0,i):
                if nums[i] > nums[j]:
                    tmax = max(tmax,dp[j]+1)
            dp[i] = tmax
        return max(dp)

    def hindex(self,citations):
        N = len(citations)
        l,r = 0,N-1
        citations.sort()
        H = 0
        while l <= r:
            mid = (l+r) >> 1
            H = max(H,min(citations[mid],N-mid))
            if citations[mid] < N-mid:
                l = mid+1
            else:
                r = mid -1
        return H

    def kthsmall(self,root,k):
        self.res = None
        self.k = k
        self.helper(root)
        return self.res

    def helper(self,root):
        if not root:return None
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right)


    def countTreeNode(self,root):
        if not root:return 0
        left,right = map(self.get_height,(root.left,root.right))
        if left == right:return 2**left + self.countTreeNode(root.right)
        else:return 2** right + self.countTreeNode(root.left)

    def get_height(self,root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height


    def searchMatrix(self,matrix,target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        y = m - 1
        x = 0
        while y >= 0 and x < n:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                x += 1
            else:
                y -= 1
        return False







