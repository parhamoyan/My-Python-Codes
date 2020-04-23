def sous_ensembles(liste, k, current=0):
    global choices
    n = len(liste)
    if current == 0:
        choices = [False for i in range(n)]
    if k == 0:
        s = "{ "
        for i in range(len(liste)):
            if choices[i]:
                s += str(liste[i]) + " "
        s += "}"
        print(s)
    elif current+k <= n:
        choices[current] = True
        sous_ensembles(liste, k-1, current+1)
        choices[current] = False
        sous_ensembles(liste, k, current+1)

# test :
liste = [1,2,3,4]
sous_ensembles(liste, 2)
