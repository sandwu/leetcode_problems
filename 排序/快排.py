


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