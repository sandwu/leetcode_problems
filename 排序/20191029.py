


def quick_sort(l):
    left = 0
    right = len(l)-1
    return q_sort(l,left,right)

def q_sort(l, left, right):
    if left < right:
        pivot = partition(l, left, right)
        q_sort(l, left, pivot-1)
        q_sort(l, pivot+1, right)
    return l


def partition(l, left, right):
    pivot = l[left]

    while left<right:
        while pivot <= l[right] and left < right:
            right -= 1
        l[left] = l[right]
        while pivot >= l[left] and left < right:
            left += 1
        l[right] = l[left]
    l[left] = pivot
    return left

l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]

print(quick_sort(l))



def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left,right)

def merge(left,right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]

    res += right[j:]
    return res


l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]

print(merge_sort(l))