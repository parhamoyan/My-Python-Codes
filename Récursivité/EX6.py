def determinant(matrice):
    if len(matrice[0]) == 1:
        res =  matrice[0][0]
    else:
        res = sum([(-1)**i*matrice[0][i]*determinant(\
            [matrice[ligne][0:i]+matrice[ligne][i+1:len(matrice)]\
             for ligne in range(1,len(matrice))]) for i in range(len(matrice))])
    return res
# test :
"""
matrice = [[6,1,1],[4,-2,5],[2,8,7]]
print(determinant(matrice))
"""
