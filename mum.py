def accum(s):
    op = ""
    for i, c in enumerate(s):
        op = op + s[i].upper() + ((s[i].lower()*i) + "-")
    return op[:-1]

accum("ZpglnRxqenU")

'''
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
'''
