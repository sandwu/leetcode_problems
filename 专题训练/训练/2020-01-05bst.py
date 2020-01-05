


def isBadversion(x):
    pass


class Solution:
    def firstbadversion(self,n):
        left = 0
        right = n
        while left <= right:
            mid = (left+right) >> 1
            if isBadversion(mid):
                if isBadversion(mid-1):
                    right = mid - 1
                else:
                    return mid
            else:
                if isBadversion(mid+1):
                    return mid + 1
                else:
                    left = mid + 1



    def kthsmallthelement(self,root,k):
        self.res = None
        self.k = k
        self.helper(root)
        return self.res

    def helper(self,root):
        if not root:return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            return root.val
        self.helper(root.right)

    def searchmatrix(self,matrix,target):
        n = len(matrix)
        if not n:return False
        m = len(matrix[0])
        if not m:return False
        y = n-1
        x = 0
        while y>=0 and x <m:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                x += 1
            else:
                y -= 1
        return False

    def hindex(self,citations):
        citations.sort()
        n = len(citations)
        h = 0
        for i,v in enumerate(citations):
            h = max(h,min(n-i,v))
        return h

    def hindex2(self,cications):
        cications.sort()
        n = len(cications)
        h = 0
        l,r = 0,n-1
        while l<=r:
            mid = (l+r) >> 1
            h = max(h,min(n-mid,cications[mid]))
            if n-mid>cications[mid]:
                l = mid+1
            else:
                r = mid-1
        return h


    def countNode(self,root):
        if not root:return 0
        left,right = map(self.get_height,(root.left,root.right))
        if left == right:return 2**left+self.countNode(root.right)
        else:return 2 ** right + self.countNode(root.left)

    def get_height(self,root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def longestsequence(self,nums):
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1,len(nums)):
            tmax = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    tmax = max(tmax,dp[j] + 1)
            dp[i] = tmax
        return max(dp)


