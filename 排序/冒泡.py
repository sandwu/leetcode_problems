


def bubblingsort(l):
    for _ in range(len(l),-1,-1):
        for j in range(1,len(l)):
            if l[j-1] > l[j]:
                l[j-1],l[j] = l[j], l[j-1]
    return l


l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1]

print(bubblingsort(l))
