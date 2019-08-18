def accum(s):
    op = ""
    for i, _ in enumerate(range(len(s))):
        op = op + str(s[i]*(i+1))
        op = op + "-" 
        print(op)

accum("ZpglnRxqenU")