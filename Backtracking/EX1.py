def sous_ensembles(liste, current=0):
    global choices
    if current == 0:
        choices = [True for i in range(len(liste))]
    if current == len(liste):
        s = "{ "
        for i in range(len(liste)):
            if choices[i]:
                s += str(liste[i]) + " "
        s += "}"
        print(s)
    else:
        choices[current] = False
        sous_ensembles(liste, current+1)
        choices[current] = True
        sous_ensembles(liste, current+1)

# test :
liste = [1,2,3,4]
sous_ensembles(liste)
