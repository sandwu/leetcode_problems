




def insertsort(l):
    for i in range(1,len(l)):
        for j in range(i,-1,-1):
            if l[j-1] > l[j]:
                l.insert(j-1,l.pop(j))
            else:
                break
    return l



l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]

print(insertsort(l))