



def bubble_sort(l):
    for i in range(len(l)-1,-1,-1):
        flag = 0
        for j in range(i):
            if l[j+1] < l[j]:
                l[j+1],l[j] = l[j],l[j+1]
                flag = 1
        if flag ==0:
            return l
    return l

def insert_sort(l):
    for i in range(len(l)):
        for j in range(i,0,-1):
            if l[j-1] > l[j]:
                l[j-1],l[j] = l[j],l[j-1]
            else:
                break
    return l



def quick_sort(l):
    left = 0
    right = len(l)-1
    return q_sort(l,left,right)

def q_sort(l,left,right):
    if left<right:
        pivot = partition(l,left,right)
        q_sort(l,0,pivot-1)
        q_sort(l,pivot+1,right)
    return l

def partition(l,left,right):
    pivot = l[left]
    while left < right:
        while left < right and l[right] >= pivot:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] <= pivot:
            left += 1
        l[right] = l[left]
    l[left] = pivot
    return left


def split_merge_sort(l):
    if len(l) == 1:return l
    mid = len(l) // 2
    left = split_merge_sort(l[:mid])
    right = split_merge_sort(l[mid:])
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
    res += left[i:] or right[j:]
    return res



l1 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
l2 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
l3 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
l4 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
print(quick_sort(l1))
print(insert_sort(l2))
print(bubble_sort(l3))
print(split_merge_sort(l4))