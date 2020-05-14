def gapInsertionSort(alist, start, gap):
    for index in range(start+gap, len(alist), gap):
        key = alist[index]
        pos = index
        while pos>=gap and alist[pos-gap]>key:
            alist[pos] = alist[pos-gap]
            pos -= gap
        alist[pos] = key

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount>0:
        for startpos in range(sublistcount):
            gapInsertionSort(alist, startpos, sublistcount)
        sublistcount = sublistcount//2
    return alist

# test :
alist = list(range(10,0,-1))
print(shellSort(alist))
