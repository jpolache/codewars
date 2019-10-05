def multiples(m, n):
    op = []
    #print(m, n)
    for i, num in enumerate(range(m)):
        #print(str(n), str(i))
        op.append(n*(i+1))
    print("vec!" + str(op))

multiples(3, 5) #vec![5, 10, 15]
multiples(4, 6) #vec![6, 12, 18, 24]

'''
def multiples(m, n):
    return [i * n for i in range(1, m+1)]
'''