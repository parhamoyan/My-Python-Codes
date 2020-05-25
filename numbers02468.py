import timeit

def fonc1(alist=[0, 2, 4, 6, 8], res=""):
    if len(res)==3:
        print(res)
    else:
        for e in alist:
            if str(e) not in res:
                if e != 0 or len(res) != 0:
                    fonc(alist, res+str(e))

def fonc2():
    res = []
    n = 0
    for i in range(2,10,2):
        a = str(i)
        for j in range(0,10,2):
            if str(j) not in a:
                b = a + str(j)
                for k in range(0,10,2):
                    if str(k) not in b:
                        c = b + str(k)
                        res.append(c)
    return res

def fonc3():
    alist = [str(i) for i in range(2,10,2)]
    blist = [i+str(j) for i in alist for j in range(0,10,2) if str(j) != i]
    clist = [i+str(j) for i in blist for j in range(0,10,2) if str(j) not in i]
    return clist

def fonc4():
    ranges = [str(i) for i in range(0,10,2)]
    alist = [str(i) for i in range(2,10,2)]
    blist = [i+j for i in alist for j in ranges if j != i]
    clist = [i+j for i in blist for j in ranges if j not in i]
    return clist

def fonc5():
    lis = []
    for i in range(100,1000):
        lis.append(str(i))
    tup=('0','2','4','8','6')
    lisss=list(filter(lambda x :x[0]  in tup and x[1] in tup and x[2] in tup ,lis))

print(timeit.timeit(lambda: fonc4(), number = 1)*100000)
print(timeit.timeit(lambda: fonc5(), number = 1)*100000)
