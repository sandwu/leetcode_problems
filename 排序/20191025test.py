


def bubblingsort(l):
    """
    time O(n) space O(1) stable
    :param l:
    :return:
    """
    for i in range(len(l),-1,-1):
        flag = False
        for j in range(1,i):
            if l[j] < l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
                flag = True
        if not flag:
            return l
    return l

def choosesort(l):
    """
    time O(n) space O(1) stable
    :param l:
    :return:
    """
    for i in range(1,len(l)):
        for j in range(len(l)):
            if l[i] < l[j]:
                l[i],l[j] = l[j],l[i]
    return l


def insertsort(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j] < l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
    return l

l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]
print("bubble",bubblingsort(l))
print("choose",choosesort(l))
print("insert",insertsort(l))