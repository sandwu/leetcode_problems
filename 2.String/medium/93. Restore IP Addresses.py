
class Solution(object):
    """
    DFS回溯来实现，注意判断条件即可
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Restore IP Addresses.
    Memory Usage: 11.9 MB, less than 5.09% of Python online submissions for Restore IP Addresses.
    """
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, s, 4, [])
        return ['.'.join(x) for x in ans]

    def helper(self, ans, s, k, temp):
        if len(s) > k* 3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3, len(s) - k + 1)):
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.helper(ans, s[i + 1:], k - 1, temp + [s[:i + 1]])


