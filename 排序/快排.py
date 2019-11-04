


def quick_sort(l):
    left = 0
    right = len(l)-1
    return q_sort(l, left, right)


def q_sort(l, left, right):
    if left<right:
        pivot = partition(l,left,right)
        q_sort(l, left, pivot-1)
        q_sort(l,pivot + 1,right)
    return l



def partition(l, left, right):
    pivot = l[left]

    while left < right:
        while left <right and l[right] >= pivot:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] <= pivot:
            left += 1
        l[right] = l[left]
    l[left] = pivot
    return left

l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]

print(quick_sort(l))

nums = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]
def quick_sort2(nums):
   if len(nums) <= 1:
       return nums
   # 随意选取一个基准数，比如选取列表第一个数
   base = nums[0]
   # left列表为nums中比基准数base小或等于base的数组成的列表
   left = [x for x in nums[1:] if x <= base]
   # right列表为nums中比基准数base大的数组成的列表
   right = [x for x in nums[1:] if x > base]
   # 对left和right列表递归排序
   return quick_sort(left) + [base] + quick_sort(right)

print(quick_sort2(nums))

print()