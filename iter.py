l = [1, 2, 3, 4, 5]
for i in range(0, len(l), 2):
    if i+1 < len(l):
        print(l[i],  l[i+1])
    else:
        print(l[i])
 #[(1, 2), (3, 4), )(5, None)]