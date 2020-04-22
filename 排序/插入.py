




def insertsort(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j-1] > l[j]:
                l.insert(j-1,l.pop(j))
                # l[j-1],l[j] = l[j],l[j-1]
            else:
                break
    return l



l = [1,3,5,7,6,4,3,1,8,8,9,2,5,1,3,1,6,2]
l1 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]

print(insertsort(l1))