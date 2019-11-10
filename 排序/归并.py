


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


def sort1(l):

    if len(l) <= 1:
        return l
    mid = len(l) // 2
    # print(start,end,mid)
    left = sort1(l[:mid])
    right = sort1(l[mid:])
    return merge(left,right)


l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2,3]

print(sort1(l))