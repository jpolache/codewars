def beggars(values, n):
    op = []
    for i in range(n): # list
        o_val = 0
        for val in (values[i::n]): #sublist
            o_val += val
        op.append(o_val)    
    return op
    
'''
def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]
'''
print("b1: ", beggars([1,2,3,4,5],1)) #,[15]
print("b2: ", beggars([1,2,3,4,5],2)) #[9,6]
