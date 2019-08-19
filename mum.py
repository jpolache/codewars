def accum(s):
    op = ""
    for i, _ in enumerate(range(len(s))):
        if s[i].upper() not in op.upper():
            op = op + s[i].upper()

        op = op + s[i].lower()*i
        if s[-1] not in op:
            op = op + "-"
        print(op)

accum("ZpglnRxqenU")