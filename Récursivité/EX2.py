def mirror(alist, index=0):
    if index<len(alist)/2-1:
        mirror(alist, index+1)
    alist[-index-1], alist[index] = alist[index], alist[-index-1]
    return alist

# test :
alist = [1,2,3,4,5,6,7,8,9,10]
print(mirror(alist))
