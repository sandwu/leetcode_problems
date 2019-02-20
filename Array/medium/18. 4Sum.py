import collections
import itertools


class Solution(object):
    """
    直接沿用3Sum的解法，多添加一层罢了，所以效率也是低的不行，不过这种方法算是最容易想出的。
    Runtime: 808 ms, faster than 22.63% of Python online submissions for 4Sum.
    Memory Usage: 10.7 MB, less than 100.00% of Python online submissions for 4Sum.
    """
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c, d = b+1, len(nums)-1
                while c < d:
                    tot = nums[a]+nums[b]+nums[c]+nums[d]
                    if tot == target:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                    if tot <= target:
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
                    if tot >= target:
                        d -= 1
                        while nums[d] == nums[d+1] and c < d:
                            d -= 1
        return ans


class Solution(object):
    """
    这里采用python的高级解法，这些用法看的我眼花缭乱，感觉自己学了一个假python；
    通过defaultdict建立字典，可以在key不存在时不报错，而是默认value为list即空列表；
    用combinations找出所有的index、value能构成的二元元祖；
    接着遍历two_sum的key，也就是nums任意两个数的和，因为value是set，所以接下来都是围绕set的操作；
    set.isdisjoint是求交集，即两个set没有相同的部分返回真，所以完美规避了两个pair相同；
    pair1|pair2则是求并集，即两个set的所有元素，；
    这里的sorted也是必备的，需要把不同的索引但是重复的数字给删除了；
    关于del two_sum[t]，也可以不删除，因为去掉这句代码照常运行，不过速度会慢点，这点还不清楚原因。
    Runtime: 168 ms, faster than 70.47% of Python online submissions for 4Sum.
    Memory Usage: 23.5 MB, less than 100.00% of Python online submissions for 4Sum.
    """
    def fourSum(self, nums, target):
        two_sum = collections.defaultdict(list)
        res = set()
        for (n1, i1), (n2, i2) in itertools.combinations(enumerate(nums), 2):
            two_sum[i1+i2].append({n1, n2})
        for t in list(two_sum.keys()):
            if not two_sum[target-t]:
                continue
            for pair1 in two_sum[t]:
                for pair2 in two_sum[target-t]:
                    if pair1.isdisjoint(pair2):
                        res.add(tuple(sorted(nums[i] for i in pair1 | pair2)))
            del two_sum[t]
        return [list(r) for r in res]