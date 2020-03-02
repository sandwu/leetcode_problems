

class Solution:
    def Twosum2(self,numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]  #答案返回值并不是索引，而是认为的计数
            elif res < target:
                left += 1
            else:
                right -= 1