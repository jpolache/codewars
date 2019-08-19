def accum(s):
    op = ""
    for i, _ in enumerate(range(len(s))):
        #if s[i].upper() not in op.upper():
        op = op + s[i].upper()
        op = op + ((s[i].lower()*i) + "-")
        #op = op[:-1]
        print(op[:-1])

accum("ZpglnRxqenU")