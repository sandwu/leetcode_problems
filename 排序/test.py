#冒泡
#date : 2019-09-02
def bubble_sort(l):
    n = len(l)
    while n>0:
        flag = 1
        for j in range(1,n):
            if l[j-1] > l[j]:
                flag = 0
                l[j-1],l[j] = l[j],l[j-1]
        n = n - 1
        if flag:
            return l
    return l

def choose_sort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    return l

l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]

print("bubble",bubble_sort(l))
print("choose",choose_sort(l))

#date : 2019-09-03

def insert_sort(l):
    for i in range(1,len(l)):
        for j in range(i-1,-1,-1):
            if l[j] <= l[i]:
                break
            else:
                l.insert(j,l.pop(i))
    return l

print('insert_sort',insert_sort(l))


def merge(left,right):
    i,j,res = 0,0,[]
    while i<len(left) and j < len(right):
        if left[i] < left[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(left[j])
            j += 1
    if left:
        res += left
    else:
        res += right
    return res

def sort1(l):

    if len(l) <= 1:
        return l
    mid = len(l) // 2
    # print(start,end,mid)
    left = sort1(l[:mid])
    right = sort1(l[mid:])
    return merge(left,right)

print('merge_sort',sort1(l))