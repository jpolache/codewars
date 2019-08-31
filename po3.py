#Given a positive integer N, return the largest integer k such that 3^k < N.
#[ e**2 for e in a_list if type(e) == types.IntType ]

def largestPower(N):
    #print([k for k in reversed(range(N)) if 3**k < N][0])
    #print(str(N))
    print(list(filter(lambda k : (3**k < N), reversed(range(N))))[0])
    

largestPower(3) #, 0)
largestPower(4) #, 1)
largestPower(1500)