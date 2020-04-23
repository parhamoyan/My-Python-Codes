def maximum(alist, index=0):
    if index == len(alist)-1:
        max = alist[index]
    else:
        max = maximum(alist, index+1)
        if max<alist[index]:
            max = alist[index]
    return max

# test :
alist = [6,9,5,4,3,10,4,3]
print(maximum(alist))
