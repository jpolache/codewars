def tidyNumber(n):
    op = True
    nlist =  [int(x) for x in str(n)]
    for i, num in enumerate(nlist):
        try:
            if nlist[i] > nlist[i+1]:
                op = False
        except:
            pass
    return op


tidyNumber(9672)
tidyNumber(2789)
