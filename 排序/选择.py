


def choosesort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j] < l[i]:
                l[i],l[j] = l[j], l[i]
    return l


l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1]

print(choosesort(l))
