

def choose_sort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[j],l[i] = l[i],l[j]
    return l


def bubble_sort(l):
    for i in range(len(l),-1,-1):
        flag = 1
        for j in range(1,i):
            if l[j-1]>l[j]:
                l[j-1],l[j] = l[j],l[j-1]
                flag = 0
        if flag == 1:
            return l
    return l

def insert_sort(l):
    for i in range(1,len(l)):
        for j in range(i,-1,-1):
            if l[j-1]>l[j]:
                l.insert(j-1,l.pop(j))
            else:
                break
    return l
l1 = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]
l2 = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]
l3 = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]
print("bubble",bubble_sort(l1))
print("choose",choose_sort(l2))
print("insert",insert_sort(l3))

def quick_sort(l):
    left = 0
    right = len(l)-1
    return q_sort(l,left,right)

def q_sort(l,left,right):
    if left<right:
        pivot = partition(l,left,right)
        q_sort(l,left,pivot-1)
        q_sort(l, pivot+1,right)
    return l

def partition(l,left,right):
    pivot = l[left]
    while left < right:
        while left<right and pivot<=l[right]:
            right -= 1
        l[left] = l[right]
        while left<right and pivot >= l[left]:
            left += 1
        l[right] = l[left]
    l[left] = pivot
    return left


def merge_sort(l):
    if len(l)<= 1:
        return l
    mid = len(l)//2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left,right)

def merge(left,right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res

l4 = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]
l5 = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]

print("amerge",merge_sort(l4))
print("aquick",quick_sort(l5))